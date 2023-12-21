# DeferredCancelEventArgs - класс
Аргументы события, обеспечивающие асинхронное ожидание с отменой изменений.
Используйте метод [InvokeNullableAsync<T>(EventHandler<T>, Object, T,
CancellationToken)](M_Tessa_Platform_PlatformExtensions_InvokeNullableAsync__1.htm)
для ожидания обработчиков такого события.
## __Definition
 **Пространство имён:** [Tessa.Platform](N_Tessa_Platform.htm)  
 **Сборка:** Tessa (в Tessa.dll) Версия: 3.6.0.17
C# __Копировать
     public class DeferredCancelEventArgs : DeferredEventArgs
VB __Копировать
     Public Class DeferredCancelEventArgs
    	Inherits DeferredEventArgs
C++ __Копировать
     public ref class DeferredCancelEventArgs : public DeferredEventArgs
F# __Копировать
     type DeferredCancelEventArgs = 
        class
            inherit DeferredEventArgs
        end
Inheritance
    [Object](https://learn.microsoft.com/dotnet/api/system.object) __[EventArgs](https://learn.microsoft.com/dotnet/api/system.eventargs) __[DeferredEventArgs](T_Tessa_Platform_DeferredEventArgs.htm) __ DeferredCancelEventArgs
Derived
[Tessa.UI.Files.FileControlCancelEventArgs](T_Tessa_UI_Files_FileControlCancelEventArgs.htm)
[Tessa.UriLinks.UriLinkEventArgs](T_Tessa_UriLinks_UriLinkEventArgs.htm)
##  __Конструкторы
[DeferredCancelEventArgs](M_Tessa_Platform_DeferredCancelEventArgs__ctor.htm)|
Создаёт экземпляр класса с указанием значений его свойств.  
---|---  
## __Свойства
[Cancel](P_Tessa_Platform_DeferredCancelEventArgs_Cancel.htm)|  Признак того,
что действие отменяется.  
---|---  
## __Методы
[Defer](M_Tessa_Platform_DeferredEventArgs_Defer.htm)|  Возвращает объект,
обеспечивающий ожидание действия. Вызовите метод в блоке using, внутри
которого выполняйте любые ожидания await.  
(Унаследован от [DeferredEventArgs](T_Tessa_Platform_DeferredEventArgs.htm))  
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
[IsPropertyChanged](M_Tessa_UI_Controls_PropertyChangedHelper_IsPropertyChanged.htm)|
Проверяет наступление события изменения свойства propertyName  
(Определяется
[PropertyChangedHelper](T_Tessa_UI_Controls_PropertyChangedHelper.htm))  
[Set](M_Tessa_Extensions_Default_Client_EDS_ComHelper_Set.htm)|  
(Определяется
[ComHelper](T_Tessa_Extensions_Default_Client_EDS_ComHelper.htm))  
##  __См. также
#### Ссылки
[Tessa.Platform - пространство имён](N_Tessa_Platform.htm)
