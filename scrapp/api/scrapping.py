from bs4 import BeautifulSoup
from requests_html import HTMLSession

s=HTMLSession()
categories=['business','engineering','design','analyst','movie','singer','dancer','drama','frontend','backend','actor','sales','executive','developer','manager','analytics']
class Job():
    def __init__(self,site,name,company,location,start_date,details,deadline):
        self.site=site
        self.name=name
        self.company=company
        self.location=location
        self.deadline=deadline
        self.start_date=start_date
        self.details=details
def get_all_urls(soup):
    links=[]
    for link in soup.find_all('a'):
        links.append(link.get('href'))
    return links
def get_internshala_details():
    intershala_job_list=[]
    base_url="https://internshala.com"
    url="/fresher-jobs"
    r=s.get(base_url+url)

    soup=BeautifulSoup(r.text,'html.parser')


    jobs=soup.find_all('div',{'class':'individual_internship'})[:10]
    for job in jobs:
        curr_category=[]
        name=' '.join(job.find('div',{'class':'heading_4_5 profile'}).text.split())
        for category in categories:
            if category in name.lower():
                curr_category.append(category)
        company=' '.join(job.find('div',{'class':'heading_6 company_name'}).text.split())
        location=job.find('a',{'class':'location_link'}).text
        additional_details=job.find_all('div',{'class':'item_body'})
        for index in range(0,len(additional_details),3):
            start_date=' '.join(additional_details[index].text.split())
            deadline=' '.join(additional_details[index+2].text.split())
        button_url=job.find('a',{'class':'view_detail_button'})['href']
        url=button_url
        r=s.get(base_url+url)

        soup=BeautifulSoup(r.text,'html.parser')
        details=soup.find_all('div',{'class':'text-container'})[2].text
        job=Job("internshala",name,company,location,start_date,details,deadline)
        intershala_job_list.append(job)
    links=get_all_urls(soup)
    interesting_urls=[]
    non_interesting_urls=[]

    for link in links:
        if link:
            if link[0]=='/':
                index=link.find('/',1)
                if link[1:index]=='fresher-job' or link[1:index]=='fresher-jobs' or link[1:index]=='internships' or link[1:index]=='internship':
                    interesting_urls.append(base_url+link)
                else:
                    non_interesting_urls.append(base_url+link)
            else:
                if 'https://internshala.com/' in link:
                    index=link.find('/',25)
                    if link[24:index]=='fresher-job' or link[24:index]=='fresher-jobs' or link[24:index]=='internships' or link[24:index]=='internship':
                        interesting_urls.append(link)
                    else:
                        non_interesting_urls.append(link)
                else:
                    non_interesting_urls.append(link)
    return non_interesting_urls
def get_talentrack_details():
    talentrack_job_list=[]
    base_url='https://www.talentrack.in/'
    r=s.get(base_url)
    soup=BeautifulSoup(r.text,'html.parser')

    curr_category=[]

    jobs=soup.find_all('div',{'class':'col-xs-4'})[3:13]
    for job in jobs:
        name=job.find('span',{'class':'job-title'}).text
        for category in categories:
            if category in name.lower():
                curr_category.append(category)
        location=' '.join(job.find('span',{'class':'job-location'}).text.split()[1:])
        start_date=job.find('span',{'class':'job-date'}).text.split()[-1]
        detailsUrl=job.find('a',{'class':'min-button-style'})['href']

        r=s.get(base_url+detailsUrl)
        soup=BeautifulSoup(r.text,'html.parser')
        details=soup.find('div',{'class':'appjobdetail'})
        descr=details.find('p',{'class':'pt-10'}).text
        deadline=details.find_all('td',{'class':'perc60 vtop'})[1].text
        company=details.find('span',{'class':'rec_det_nam'}).text
        job=Job("talentrack",name,company,location,start_date,descr,deadline)
        talentrack_job_list.append(job)
    links=get_all_urls(soup)
    interesting_url=[]
    non_interesting_url=[]
    for link in links:
        if link:
            if '/jobdetail' in link or '/all-job-in-india' in link or '/actor' in link or '/model' in link:
                interesting_url.append(base_url+link)
            else:
                if 'https://' in link:
                    non_interesting_url.append(link)
                else:
                    non_interesting_url.append(base_url+link)
    return non_interesting_url
def get_iimjobs_details():
    iimjobs_job_list=[]
    base_url='https://www.iimjobs.com/c/it--systems-jobs-15.html'
    r=s.get(base_url)
    soup=BeautifulSoup(r.text,'html.parser')
    links=get_all_urls(soup)
    jobList=[]
    jobs=soup.find_all('div',{'class':'jobRow'})[:10]
    for job in jobs:
        if job:
            curr_category=[]
            a_tag=job.find('a',{'name':'view_link'})
            start_date=job.find('span',{'class':'gry_txt'}).text
            if a_tag:
                name=a_tag.text
                for category in categories:
                    if category in name.lower():
                        curr_category.append(category)
                detailsUrl=a_tag['href']
                r=s.get(detailsUrl)
                soup=BeautifulSoup(r.text,'html.parser')

                location=soup.find('span',{'class':'jobloc'}).text.split()[-1]
                company_tag=soup.find_all('span',{'class':'mt5'})[3]
                index=company_tag.text.split().index('at')
                company=' '.join(company_tag.text.split()[index+1:])
                if 'Locations/' in location:
                    location=location.replace('Locations/','')
                details=soup.find('div',{'class':'details'}).text.split(':')
                required=None
                for index in range(len(details)):
                    if not "job description" in details[index].lower():
                        if "job profile" in details[index].lower() or "description" in details[index].lower()or "responsibilities" in details[index].lower() or "role" in details[index].lower():
                            required=details[index+1]
                            break
                job=Job("iimjobs",name,company,location,start_date,required,"")
                iimjobs_job_list.append(job)
    interesting_urls=[]
    non_interesting_urls=[]
    for link in links:
        if link:
            if "https://www.iimjobs.com/j" in link or "https://www.iimjobs.com/c" in link or "https://www.iimjobs.com/k" in link:
                interesting_urls.append(link)
            else:
                non_interesting_urls.append(link)
    return non_interesting_urls

                
                





    
