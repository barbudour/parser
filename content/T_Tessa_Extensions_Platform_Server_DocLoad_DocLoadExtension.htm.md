# DocLoadExtension - класс
Базовый класс для расширения для потокового ввода.
## __Definition
 **Пространство имён:**
[Tessa.Extensions.Platform.Server.DocLoad](N_Tessa_Extensions_Platform_Server_DocLoad.htm)  
 **Сборка:** Tessa (в Tessa.dll) Версия: 3.6.0.17
C# __Копировать
     public class DocLoadExtension : IDocLoadExtension
VB __Копировать
     Public Class DocLoadExtension
    	Implements IDocLoadExtension
C++ __Копировать
     public ref class DocLoadExtension : IDocLoadExtension
F# __Копировать
     type DocLoadExtension = 
        class
            interface IDocLoadExtension
        end
Inheritance
    [Object](https://learn.microsoft.com/dotnet/api/system.object) __ DocLoadExtension
Derived
[Tessa.Extensions.Default.Server.Cards.DefaultDocLoadExtension](T_Tessa_Extensions_Default_Server_Cards_DefaultDocLoadExtension.htm)
Implements
    [IDocLoadExtension](T_Tessa_Extensions_Platform_Server_DocLoad_IDocLoadExtension.htm)
##  __Конструкторы
[DocLoadExtension](M_Tessa_Extensions_Platform_Server_DocLoad_DocLoadExtension__ctor.htm)|
Инициализирует новый экземпляр класса DocLoadExtension  
---|---  
##  __Методы
[Equals](https://learn.microsoft.com/dotnet/api/system.object.equals#system-
object-equals\(system-object\))| Determines whether the specified object is
equal to the current object.  
(Унаследован от
[Object](https://learn.microsoft.com/dotnet/api/system.object))  
---|---  
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
[IsScanFile](M_Tessa_Extensions_Platform_Server_DocLoad_DocLoadExtension_IsScanFile.htm)|
Метод, фильтрующий файлы в директории.  
[MemberwiseClone](https://learn.microsoft.com/dotnet/api/system.object.memberwiseclone#system-
object-memberwiseclone)| Creates a shallow copy of the current
[Object](https://learn.microsoft.com/dotnet/api/system.object).  
(Унаследован от
[Object](https://learn.microsoft.com/dotnet/api/system.object))  
[Request](M_Tessa_Extensions_Platform_Server_DocLoad_DocLoadExtension_Request.htm)|
Метод для выполнения действия по штрих-коду. Должен получить идентификатор
карточки по штрих-коду, указанному в контексте, и установить его в свойстве
контекста.  
[Save](M_Tessa_Extensions_Platform_Server_DocLoad_DocLoadExtension_Save.htm)|
Метод для выполнения сохранения документа в карточку.  
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
[Tessa.Extensions.Platform.Server.DocLoad - пространство
имён](N_Tessa_Extensions_Platform_Server_DocLoad.htm)
