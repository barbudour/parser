# CardGetFileContentExtension - класс
Базовый класс для расширения для процесса получения контента файла.
## __Definition
 **Пространство имён:** [Tessa.Cards.Extensions](N_Tessa_Cards_Extensions.htm)  
 **Сборка:** Tessa (в Tessa.dll) Версия: 3.6.0.17
C# __Копировать
     public abstract class CardGetFileContentExtension : ICardGetFileContentExtension, 
    	ICardExtension, IExtension
VB __Копировать
     Public MustInherit Class CardGetFileContentExtension
    	Implements ICardGetFileContentExtension, ICardExtension, IExtension
C++ __Копировать
     public ref class CardGetFileContentExtension abstract : ICardGetFileContentExtension, 
    	ICardExtension, IExtension
F# __Копировать
     [<AbstractClassAttribute>]
    type CardGetFileContentExtension = 
        class
            interface ICardGetFileContentExtension
            interface ICardExtension
            interface IExtension
        end
Inheritance
    [Object](https://learn.microsoft.com/dotnet/api/system.object) __ CardGetFileContentExtension
Derived
[Tessa.Cards.Extensions.Templates.TaskSatelliteGetFileContentExtension](T_Tessa_Cards_Extensions_Templates_TaskSatelliteGetFileContentExtension.htm)
[Tessa.Extensions.Default.Client.Files.ClientFileTemplatePermissionsGetFileContentExtension](T_Tessa_Extensions_Default_Client_Files_ClientFileTemplatePermissionsGetFileContentExtension.htm)
[Tessa.Extensions.Default.Client.Files.ClientKrPermissionsGetFileContentExtension](T_Tessa_Extensions_Default_Client_Files_ClientKrPermissionsGetFileContentExtension.htm)
[Tessa.Extensions.Default.Server.Files.DocLoadBarcodeGetFileContentExtension](T_Tessa_Extensions_Default_Server_Files_DocLoadBarcodeGetFileContentExtension.htm)
[Tessa.Extensions.Default.Server.Files.EmbeddedDataGetFileContentExtension](T_Tessa_Extensions_Default_Server_Files_EmbeddedDataGetFileContentExtension.htm)
[Tessa.Extensions.Default.Server.Files.ForumAttachmentsGetFileContentExtension](T_Tessa_Extensions_Default_Server_Files_ForumAttachmentsGetFileContentExtension.htm)
[Tessa.Extensions.Default.Server.Files.KrVirtualFileConvertGetContentExtension](T_Tessa_Extensions_Default_Server_Files_KrVirtualFileConvertGetContentExtension.htm)
[Tessa.Extensions.Default.Server.Files.KrVirtualFileGetContentExtension](T_Tessa_Extensions_Default_Server_Files_KrVirtualFileGetContentExtension.htm)
[Tessa.Extensions.Default.Server.Files.ServerFileTemplatePermissionsGetFileContentExtension](T_Tessa_Extensions_Default_Server_Files_ServerFileTemplatePermissionsGetFileContentExtension.htm)
[Tessa.Extensions.Default.Server.Files.ServerKrPermissionsGetFileContentExtension](T_Tessa_Extensions_Default_Server_Files_ServerKrPermissionsGetFileContentExtension.htm)
[Tessa.Extensions.Default.Server.Files.ServerPathGetFileContentExtension](T_Tessa_Extensions_Default_Server_Files_ServerPathGetFileContentExtension.htm)
[Tessa.Extensions.Platform.Client.Cards.CardTaskDialogGetFileContentExtension](T_Tessa_Extensions_Platform_Client_Cards_CardTaskDialogGetFileContentExtension.htm)
[Tessa.Extensions.Platform.Client.Cards.SetDigestGetFileContentExtension](T_Tessa_Extensions_Platform_Client_Cards_SetDigestGetFileContentExtension.htm)
[Tessa.Extensions.Platform.Server.Cards.AccessGetFileContentExtension](T_Tessa_Extensions_Platform_Server_Cards_AccessGetFileContentExtension.htm)
[Tessa.Extensions.Platform.Server.Cards.ActionHistoryGetFileExtension](T_Tessa_Extensions_Platform_Server_Cards_ActionHistoryGetFileExtension.htm)
[Tessa.Extensions.Platform.Server.Cards.CheckRequestGetFileContentExtension](T_Tessa_Extensions_Platform_Server_Cards_CheckRequestGetFileContentExtension.htm)
[Tessa.Extensions.Platform.Server.Cards.ConverterFileContentExtension](T_Tessa_Extensions_Platform_Server_Cards_ConverterFileContentExtension.htm)
[Tessa.Extensions.Platform.Server.Cards.FileSatelliteGetFileContentExtension](T_Tessa_Extensions_Platform_Server_Cards_FileSatelliteGetFileContentExtension.htm)
[Tessa.Extensions.Platform.Server.Cards.FileTemplateGetContentExtension](T_Tessa_Extensions_Platform_Server_Cards_FileTemplateGetContentExtension.htm)
[Tessa.Extensions.Platform.Server.Cards.Satellites.UniversalSatelliteGetFileContentExtension](T_Tessa_Extensions_Platform_Server_Cards_Satellites_UniversalSatelliteGetFileContentExtension.htm)
[Tessa.Extensions.Platform.Server.Export.ExportGetFileContentExtension](T_Tessa_Extensions_Platform_Server_Export_ExportGetFileContentExtension.htm)
[Tessa.UI.Cards.Extensions.Templates.TaskSatelliteClientGetFileContentExtension](T_Tessa_UI_Cards_Extensions_Templates_TaskSatelliteClientGetFileContentExtension.htm)
Подробнее __Less __
Implements
    [ICardExtension](T_Tessa_Cards_Extensions_ICardExtension.htm), [ICardGetFileContentExtension](T_Tessa_Cards_Extensions_ICardGetFileContentExtension.htm), [IExtension](T_Tessa_Extensions_IExtension.htm)
##  __Конструкторы
[CardGetFileContentExtension](M_Tessa_Cards_Extensions_CardGetFileContentExtension__ctor.htm)|
Инициализирует новый экземпляр класса CardGetFileContentExtension  
---|---  
##  __Методы
[AfterRequest](M_Tessa_Cards_Extensions_CardGetFileContentExtension_AfterRequest.htm)|
Действие, выполняемое после получения контента файла как при успешном, так и
при неудачном результате.  
---|---  
[AfterRequestFinally](M_Tessa_Cards_Extensions_CardGetFileContentExtension_AfterRequestFinally.htm)|
Действие, выполняемое при возникновении исключения или после получения
контента файла как при успешном, так и при неудачном результате.
Необработанные исключения не прерывают выполнение цепочки расширений.  
[BeforeRequest](M_Tessa_Cards_Extensions_CardGetFileContentExtension_BeforeRequest.htm)|
Действие, выполняемое перед получением контента файла стандартными средствами.
Может установить ответ на запрос и функцию получения контента для того, чтобы
получение контента стандартными средствами не выполнялось.  
[Equals](https://learn.microsoft.com/dotnet/api/system.object.equals#system-
object-equals\(system-object\))| Determines whether the specified object is
equal to the current object.  
(Унаследован от
[Object](https://learn.microsoft.com/dotnet/api/system.object))  
[Finalize](https://learn.microsoft.com/dotnet/api/system.object.finalize#system-
object-finalize)| Allows an object to try to free resources and perform other
cleanup operations before it is reclaimed by garbage collection.  
(Унаследован от
[Object](https://learn.microsoft.com/dotnet/api/system.object))  
[GetHashCode](https://learn.microsoft.com/dotnet/api/system.object.gethashcode#system-
object-gethashcode)| Serves as the default hash function.  
(Унаследован от
[Object](https://learn.microsoft.com/dotnet/api/system.object))  
[GetType](https://learn.microsoft.com/dotnet/api/system.object.gettype#system-
object-gettype)| Gets the
[Type](https://learn.microsoft.com/dotnet/api/system.type) of the current
instance.  
(Унаследован от
[Object](https://learn.microsoft.com/dotnet/api/system.object))  
[MemberwiseClone](https://learn.microsoft.com/dotnet/api/system.object.memberwiseclone#system-
object-memberwiseclone)| Creates a shallow copy of the current
[Object](https://learn.microsoft.com/dotnet/api/system.object).  
(Унаследован от
[Object](https://learn.microsoft.com/dotnet/api/system.object))  
[ToString](https://learn.microsoft.com/dotnet/api/system.object.tostring#system-
object-tostring)| Returns a string that represents the current object.  
(Унаследован от
[Object](https://learn.microsoft.com/dotnet/api/system.object))  
##  __Методы расширения
[Get](M_Tessa_Extensions_Default_Client_EDS_ComHelper_Get.htm)|  
(Определяется
[ComHelper](T_Tessa_Extensions_Default_Client_EDS_ComHelper.htm))  
---|---  
[InternalMarkerCanvas](M_Tessa_UI_Views_Charting_Annotations_AnnotationInternalsAccessor_InternalMarkerCanvas.htm)|
Возвращает маркер аннотации  
(Определяется
[AnnotationInternalsAccessor](T_Tessa_UI_Views_Charting_Annotations_AnnotationInternalsAccessor.htm))  
[Invoke](M_Tessa_Extensions_Default_Client_EDS_ComHelper_Invoke.htm)|  
(Определяется
[ComHelper](T_Tessa_Extensions_Default_Client_EDS_ComHelper.htm))  
[Set](M_Tessa_Extensions_Default_Client_EDS_ComHelper_Set.htm)|  
(Определяется
[ComHelper](T_Tessa_Extensions_Default_Client_EDS_ComHelper.htm))  
##  __См. также
#### Ссылки
[Tessa.Cards.Extensions - пространство имён](N_Tessa_Cards_Extensions.htm)
