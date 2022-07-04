
from icrawler.builtin import GoogleImageCrawler

a = input("Шо надо(на Английском):")
b = input("Куда качать:")
c = input("Сколько штук:")
d = input("Искать старые фото(y или n):")

if d == "y":
    filters = dict(
        color="blackandwhite"
    )
else:
    filters = dict(
           
    )
        
def google_img_downloader():
    
    crawler = GoogleImageCrawler(storage={"root_dir":rf"{b}"})
    crawler.crawl(
        
        keyword=a,
        max_num=int(c),
        overwrite=True,
        filters=filters,
        file_idx_offset="auto",
        #min_size=(1080),
    )

def main():
    google_img_downloader()

if __name__ == "__main__":
    main()


