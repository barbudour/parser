# KrVirtualFileManager - класс
Объект для получения информации о виртуальных файлах по карточке и проверки
доступа к файлам.
## __Definition
 **Пространство имён:**
[Tessa.Extensions.Default.Server.Files.VirtualFiles](N_Tessa_Extensions_Default_Server_Files_VirtualFiles.htm)  
 **Сборка:** Tessa.Extensions.Default.Server (в
Tessa.Extensions.Default.Server.dll) Версия: 3.6.0.17
C# __Копировать
     public sealed class KrVirtualFileManager : IKrVirtualFileManager
VB __Копировать
     Public NotInheritable Class KrVirtualFileManager
    	Implements IKrVirtualFileManager
C++ __Копировать
     public ref class KrVirtualFileManager sealed : IKrVirtualFileManager
F# __Копировать
     [<SealedAttribute>]
    type KrVirtualFileManager = 
        class
            interface IKrVirtualFileManager
        end
Inheritance
    [Object](https://learn.microsoft.com/dotnet/api/system.object) __ KrVirtualFileManager
Implements
    [IKrVirtualFileManager](T_Tessa_Extensions_Default_Server_Files_VirtualFiles_IKrVirtualFileManager.htm)
##  __Конструкторы
[KrVirtualFileManager](M_Tessa_Extensions_Default_Server_Files_VirtualFiles_KrVirtualFileManager__ctor.htm)|
Инициализирует новый экземпляр класса KrVirtualFileManager  
---|---  
##  __Методы
[CheckAccessForFileAsync](M_Tessa_Extensions_Default_Server_Files_VirtualFiles_KrVirtualFileManager_CheckAccessForFileAsync.htm)|
Метод для проверки доступа на виртуальный файл для карточки.  
---|---  
[Equals](https://learn.microsoft.com/dotnet/api/system.object.equals#system-
object-equals\(system-object\))| Determines whether the specified object is
equal to the current object.  
(Унаследован от
[Object](https://learn.microsoft.com/dotnet/api/system.object))  
[FillCardWithFilesAsync](M_Tessa_Extensions_Default_Server_Files_VirtualFiles_KrVirtualFileManager_FillCardWithFilesAsync.htm)|
Метод для установки виртуальных файлов в карточку с учетом проверок доступа.
Возвращает результат выполнения, в котором могут быть сообщения об ошибках.  
[Finalize](https://learn.microsoft.com/dotnet/api/system.object.finalize#system-
object-finalize)| Allows an object to try to free resources and perform other
cleanup operations before it is reclaimed by garbage collection.  
(Унаследован от
[Object](https://learn.microsoft.com/dotnet/api/system.object))  
[GetHashCode](https://learn.microsoft.com/dotnet/api/system.object.gethashcode#system-
object-gethashcode)| Serves as the default hash function.  
(Унаследован от
[Object](https://learn.microsoft.com/dotnet/api/system.object))  
[GetSuggestedFileNameAsync](M_Tessa_Extensions_Default_Server_Files_VirtualFiles_KrVirtualFileManager_GetSuggestedFileNameAsync.htm)|
Возвращает предпочитаемое имя файла, сгенерированного по версии файла из
шаблона. При этом заменяются плейсхолдеры в заданном шаблонизированном имени
templateFileName.  
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
[Tessa.Extensions.Default.Server.Files.VirtualFiles - пространство
имён](N_Tessa_Extensions_Default_Server_Files_VirtualFiles.htm)
