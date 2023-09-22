def extension_to_mime(file):
    file_split = file.lower().strip().split(".")
    out = ""
    match file_split[-1]:
        case "gif":
            out = "image/gif"
        case "jpg" | "jpeg":
            out = "image/jpeg"
        case "png":
            out = "image/png"
        case "pdf":
            out = "application/pdf"
        case "txt":
            out = "text/plain"
        case "zip":
            out = "application/zip"
        case "bin" | _:
            out = "application/octet-stream"

    print(out)

def main():
    file = extension_to_mime(input("File name:"))
main()