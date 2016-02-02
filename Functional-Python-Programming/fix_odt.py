"""Fix Chapter 7 and 8"""

import zipfile
import os
from xml.etree import cElementTree as XML
import glob

def extract_odt( source_path, chapter ):
    """Step 1. Unzip the .odt. Read from the dropbox path. Extract temp file to CWD"""
    basename, _= os.path.splitext(os.path.basename( chapter ))
    try:
        os.mkdir(basename)
    except OSError as ex:
        pass
    with zipfile.ZipFile(os.path.join(source_path, chapter)) as zip:
        #print( zip.namelist() )
        zip.extractall(basename)
    #for member in zip.infolist():
    #    print( member.filename, member.flag_bits )
    destination=  os.path.join(os.getcwd(),basename)
    print( "Extract .ODT to", destination )
    return basename

def parse_content_xml( basename="B03652_07_2d_SFL" ):
    """Step 2: Attempt to parse the content.xml which was extracted.
    Given the error message, manually tweak the XML to fix the
    problem.
    """
    with open(os.path.join(basename,"content.xml"), encoding='mac-roman') as content:
        body= content.read()
        # print( body )
        doc= XML.fromstring( body )
        # print( doc )
        return doc

def parse_all_xml( basename="B03652_07_2d_SFL" ):
    """Step 2, alt: Attempt to parse all XML's which were extracted.
    Given the error message, manually tweak the XML to fix the
    problem.
    """
    for path, dirlist, filelist in os.walk( basename ):
        for name in filelist:
            _, ext = os.path.splitext( name )
            if ext == ".xml":
                try:
                    XML.parse( os.path.join(path,name)  )
                    print( os.path.join(path,name) )
                except Exception as ex:
                    print( os.path.join(path,name), "***", ex )

def rebuild_odt( chapter="Chapter 7/B03652_07_2d_SFL.odt" ):
    """Step 3: Rebuild a new version of the .odt locally.

    Does not work -- something is still improper about the
    resulting ODT file.
    """
    newzip = os.path.basename( chapter )
    basename, _= os.path.splitext(os.path.basename( chapter ))
    with zipfile.ZipFile(newzip, "w", compression=zipfile.ZIP_DEFLATED) as zip:
        for path, dirlist, filelist in os.walk( basename ):
            for name in filelist:
                print( "zipping", os.path.join(path,name) )
                zip.write( os.path.join(path,name) )
            for name in dirlist:
                print( "directory", os.path.join(path,name) )
                zip.write( os.path.join(path,name) ) #??
    print("Built", newzip )

def tweak_odt( chapter="Chapter 7/B03652_07_2d_SFL.odt" ):
    """Step 3, alternate. Open ODT for writing and try to replace content.xml.

    While this produces a warning, the resulting file does appear to work.
    Once.
    Which is enough to save it in another format.
    """
    basename, _= os.path.splitext(os.path.basename( chapter ))
    with zipfile.ZipFile(os.path.join(source_path, chapter), "a") as zip:
        zip.write( os.path.join(basename, "content.xml"), "content.xml" )

dropbox= "~slott/Dropbox"
source_path = os.path.expanduser( os.path.join( dropbox, "B03652 - Functional Python Programming", "Rewrites" ) )

def fix_7():
    """Strange situation -- file damaged."""
    extract_odt( source_path, "Chapter 7/B03652_07_2d_SFL.odt" )
    parse_all_xml( "B03652_07_2d_SFL" )
    rebuild_odt( "Chapter 7/B03652_07_2d_SFL.odt"  )

def fix_8():
    """Strange situation -- file damaged."""
    extract_odt( source_path, "Chapter 8/B03652_08_2d_SFL.odt" )
    parse_all_xml( "B03652_08_2d_SFL" )
    #rebuild_odt( "Chapter 8/B03652_08_2d_SFL.odt"  )
    tweak_odt( "Chapter 8/B03652_08_2d_SFL.odt"  )

ns = dict(
    office="urn:oasis:names:tc:opendocument:xmlns:office:1.0",
    style="urn:oasis:names:tc:opendocument:xmlns:style:1.0",
    text="urn:oasis:names:tc:opendocument:xmlns:text:1.0",
    table="urn:oasis:names:tc:opendocument:xmlns:table:1.0",
    draw="urn:oasis:names:tc:opendocument:xmlns:drawing:1.0",
    fo="urn:oasis:names:tc:opendocument:xmlns:xsl-fo-compatible:1.0",
    xlink="http://www.w3.org/1999/xlink",
    dc="http://purl.org/dc/elements/1.1/",
    meta="urn:oasis:names:tc:opendocument:xmlns:meta:1.0",
    number="urn:oasis:names:tc:opendocument:xmlns:datastyle:1.0",
    svg="urn:oasis:names:tc:opendocument:xmlns:svg-compatible:1.0",
    chart="urn:oasis:names:tc:opendocument:xmlns:chart:1.0",
    dr3d="urn:oasis:names:tc:opendocument:xmlns:dr3d:1.0",
    math="http://www.w3.org/1998/Math/MathML",
    form="urn:oasis:names:tc:opendocument:xmlns:form:1.0",
    script="urn:oasis:names:tc:opendocument:xmlns:script:1.0",
    ooo="http://openoffice.org/2004/office",
    ooow="http://openoffice.org/2004/writer",
    oooc="http://openoffice.org/2004/calc",
    dom="http://www.w3.org/2001/xml-events",
    xforms="http://www.w3.org/2002/xforms",
    xsd="http://www.w3.org/2001/XMLSchema",
    xsi="http://www.w3.org/2001/XMLSchema-instance",
    rpt="http://openoffice.org/2005/report",
    of="urn:oasis:names:tc:opendocument:xmlns:of:1.2",
    xhtml="http://www.w3.org/1999/xhtml",
    grddl="http://www.w3.org/2003/g/data-view#",
    tableooo="http://openoffice.org/2009/table",
    textooo="http://openoffice.org/2013/office",
    field="urn:openoffice:names:experimental:ooo-ms-interop:xmlns:field:1.0",
    )

DRAW_FRAME= XML.QName( ns['draw'], 'frame' )
DRAW_OBJECT= XML.QName( ns['draw'], 'object' )
DRAW_NAME= XML.QName( ns['draw'], 'name' )
DRAW_IMAGE= XML.QName( ns['draw'], 'image' )
XLINK_HREF= XML.QName( ns['xlink'], 'href' )
SVG_DESC= XML.QName( ns['svg'], 'desc' )

def show_tag(tag, base_directory ):
    if tag.tag == DRAW_FRAME:
        print( ":frame:`{0}`".format(tag.attrib[DRAW_NAME]), end='' )
    if tag.tag == DRAW_IMAGE:
        print( ":image:`{0}`".format(tag.attrib[XLINK_HREF]), end='' )
    if tag.tag == DRAW_OBJECT:
        filename= tag.attrib[XLINK_HREF]
        d2= parse_content_xml( os.path.join( base_directory, filename ) )
        f= d2.find( ".//math:annotation", namespaces=ns )
        print( ":math:`{0}`:xref:`{1}`".format(f.text, filename), end='')
    if tag.tag == SVG_DESC: return
    if tag.text:
        print( tag.text, end="" )
    for t in tag:
        show_tag(t, base_directory)
    if tag.tail:
        print( tag.tail, end="" )

if __name__ == "__main__":
    search_draw= ".//text:p/draw:frame/draw:object/../.."
    source_path= ".."
    start_here= os.path.join( source_path, "B03652_[0-9][0-9]_1d.odt" )
    for chap in glob.glob(start_here):
        print()
        name= extract_odt( ".", chap )
        doc= parse_content_xml( name )
        for tag in doc.findall( ".//text:p/draw:frame/..", namespaces=ns ):
            print()
            show_tag(tag, name)
            print()
        print()