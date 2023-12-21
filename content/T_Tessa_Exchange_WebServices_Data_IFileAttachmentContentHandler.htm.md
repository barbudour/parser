# IFileAttachmentContentHandler - интерфейс
Defines a file attachment content handler. Application can implement
IFileAttachmentContentHandler to provide a stream in which the content of file
attachment should be written.
## __Definition
 **Пространство имён:**
[Tessa.Exchange.WebServices.Data](N_Tessa_Exchange_WebServices_Data.htm)  
 **Сборка:** Tessa.Server (в Tessa.Server.dll) Версия: 3.6.0.17
C# __Копировать
     public interface IFileAttachmentContentHandler
VB __Копировать
     Public Interface IFileAttachmentContentHandler
C++ __Копировать
     public interface class IFileAttachmentContentHandler
F# __Копировать
     type IFileAttachmentContentHandler = interface end
##  __Методы
[GetOutputStream](M_Tessa_Exchange_WebServices_Data_IFileAttachmentContentHandler_GetOutputStream.htm)|
Provides a stream to which the content of the attachment with the specified Id
should be written.  
---|---  
## __См. также
#### Ссылки
[Tessa.Exchange.WebServices.Data - пространство
имён](N_Tessa_Exchange_WebServices_Data.htm)
