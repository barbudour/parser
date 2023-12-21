# CardGetFileVersionsExtension - класс
Базовый класс расширений для процесса получения информации по версиям файла.
## __Definition
 **Пространство имён:** [Tessa.Cards.Extensions](N_Tessa_Cards_Extensions.htm)  
 **Сборка:** Tessa (в Tessa.dll) Версия: 3.6.0.17
C# __Копировать
     public abstract class CardGetFileVersionsExtension : ICardGetFileVersionsExtension, 
    	ICardExtension, IExtension
VB __Копировать
     Public MustInherit Class CardGetFileVersionsExtension
    	Implements ICardGetFileVersionsExtension, ICardExtension, IExtension
C++ __Копировать
     public ref class CardGetFileVersionsExtension abstract : ICardGetFileVersionsExtension, 
    	ICardExtension, IExtension
F# __Копировать
     [<AbstractClassAttribute>]
    type CardGetFileVersionsExtension = 
        class
            interface ICardGetFileVersionsExtension
            interface ICardExtension
            interface IExtension
        end
Inheritance
    [Object](https://learn.microsoft.com/dotnet/api/system.object) __ CardGetFileVersionsExtension
Derived
[Tessa.Cards.Extensions.Templates.TaskSatelliteGetFileVersionsExtension](T_Tessa_Cards_Extensions_Templates_TaskSatelliteGetFileVersionsExtension.htm)
[Tessa.Extensions.Default.Client.Files.ClientKrPermissionsGetFileVersionsExtension](T_Tessa_Extensions_Default_Client_Files_ClientKrPermissionsGetFileVersionsExtension.htm)
[Tessa.Extensions.Default.Server.Files.ErrorGetFileVersionsExtension](T_Tessa_Extensions_Default_Server_Files_ErrorGetFileVersionsExtension.htm)
[Tessa.Extensions.Default.Server.Files.ServerKrPermissionsGetFileVersionsExtension](T_Tessa_Extensions_Default_Server_Files_ServerKrPermissionsGetFileVersionsExtension.htm)
[Tessa.Extensions.Platform.Client.Cards.SetDigestGetFileVersionsExtension](T_Tessa_Extensions_Platform_Client_Cards_SetDigestGetFileVersionsExtension.htm)
[Tessa.Extensions.Platform.Server.Cards.AccessGetFileVersionsExtension](T_Tessa_Extensions_Platform_Server_Cards_AccessGetFileVersionsExtension.htm)
[Tessa.Extensions.Platform.Server.Cards.CompressCardGetFileVersionsExtension](T_Tessa_Extensions_Platform_Server_Cards_CompressCardGetFileVersionsExtension.htm)
[Tessa.Extensions.Platform.Server.Cards.Satellites.UniversalSatelliteGetFileVersionsExtension](T_Tessa_Extensions_Platform_Server_Cards_Satellites_UniversalSatelliteGetFileVersionsExtension.htm)
[Tessa.Extensions.Platform.Shared.Cards.DecompressCardGetFileVersionsExtension](T_Tessa_Extensions_Platform_Shared_Cards_DecompressCardGetFileVersionsExtension.htm)
Подробнее __Less __
Implements
    [ICardExtension](T_Tessa_Cards_Extensions_ICardExtension.htm), [ICardGetFileVersionsExtension](T_Tessa_Cards_Extensions_ICardGetFileVersionsExtension.htm), [IExtension](T_Tessa_Extensions_IExtension.htm)
##  __Конструкторы
[CardGetFileVersionsExtension](M_Tessa_Cards_Extensions_CardGetFileVersionsExtension__ctor.htm)|
Инициализирует новый экземпляр класса CardGetFileVersionsExtension  
---|---  
##  __Методы
[AfterRequest](M_Tessa_Cards_Extensions_CardGetFileVersionsExtension_AfterRequest.htm)|
Действие, выполняемое после получения версий файла как при успешном, так и при
неудачном результате.  
---|---  
[AfterRequestFinally](M_Tessa_Cards_Extensions_CardGetFileVersionsExtension_AfterRequestFinally.htm)|
Действие, выполняемое при возникновении исключения или после получения версий
файла как при успешном, так и при неудачном результате. Необработанные
исключения не прерывают выполнение цепочки расширений.  
[BeforeRequest](M_Tessa_Cards_Extensions_CardGetFileVersionsExtension_BeforeRequest.htm)|
Действие, выполняемое перед получением версий файла стандартными средствами.
Может установить ответ на запрос для того, чтобы получение версий файла
стандартными средствами не выполнялось.  
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
