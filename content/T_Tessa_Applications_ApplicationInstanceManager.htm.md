# ApplicationInstanceManager - класс
Предоставляет методы для определения, является ли текущий экземпляр приложения
первым запущенным в системе
## __Definition
 **Пространство имён:** [Tessa.Applications](N_Tessa_Applications.htm)  
 **Сборка:** Tessa (в Tessa.dll) Версия: 3.6.0.17
C# __Копировать
     public class ApplicationInstanceManager : IDisposable
VB __Копировать
     Public Class ApplicationInstanceManager
    	Implements IDisposable
C++ __Копировать
     public ref class ApplicationInstanceManager : IDisposable
F# __Копировать
     type ApplicationInstanceManager = 
        class
            interface IDisposable
        end
Inheritance
    [Object](https://learn.microsoft.com/dotnet/api/system.object) __ ApplicationInstanceManager
Implements
    [IDisposable](https://learn.microsoft.com/dotnet/api/system.idisposable)
##  __Конструкторы
[ApplicationInstanceManager](M_Tessa_Applications_ApplicationInstanceManager__ctor.htm)|
Initializes a new instance of the ApplicationInstanceManager class. Создаёт
экземпляр класса ApplicationInstanceManager.  
---|---  
## __Свойства
[IsFirstInstance](P_Tessa_Applications_ApplicationInstanceManager_IsFirstInstance.htm)|
Gets a value indicating whether Признак, является ли текущий экземпляр
приложения первым в системе  
---|---  
[IsRegisteredAsFirstInstance](P_Tessa_Applications_ApplicationInstanceManager_IsRegisteredAsFirstInstance.htm)|
Gets a value indicating whether Признак регистрации экземпляра приложения в
касечтве первого зхапущенного  
## __Методы
[Dispose](M_Tessa_Applications_ApplicationInstanceManager_Dispose.htm)|
Performs application-defined tasks associated with freeing, releasing, or
resetting unmanaged resources.  
---|---  
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
[Register](M_Tessa_Applications_ApplicationInstanceManager_Register.htm)|
Выполняет регистрация текущего экземпляра приложения в системе  
[ToString](https://learn.microsoft.com/dotnet/api/system.object.tostring#system-
object-tostring)| Returns a string that represents the current object.  
(Унаследован от
[Object](https://learn.microsoft.com/dotnet/api/system.object))  
[Unregister](M_Tessa_Applications_ApplicationInstanceManager_Unregister.htm)|
Выполняет отмену регистрации текущего экземпляра приложения в системе  
## __Методы расширения
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
[Tessa.Applications - пространство имён](N_Tessa_Applications.htm)