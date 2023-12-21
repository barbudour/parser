# HostOperation<T> \- класс
Базовый класс для операции выполняемых Tessa Host
##  __Definition
 **Пространство имён:** [Tessa.Host](N_Tessa_Host.htm)  
 **Сборка:** Tessa (в Tessa.dll) Версия: 3.6.0.17
C# __Копировать
     public abstract class HostOperation<T> : IHostOperation<T>, 
    	IDisposable
    where T : IHostOperationContext
VB __Копировать
     Public MustInherit Class HostOperation(Of T As IHostOperationContext)
    	Implements IHostOperation(Of T), IDisposable
C++ __Копировать
    generic<typename T>
    where T : IHostOperationContext
    public ref class HostOperation abstract : IHostOperation<T>, 
    	IDisposable
F# __Копировать
     [<AbstractClassAttribute>]
    type HostOperation<'T when 'T : IHostOperationContext> = 
        class
            interface IHostOperation<'T>
            interface IDisposable
        end
Inheritance
    [Object](https://learn.microsoft.com/dotnet/api/system.object) __ HostOperation<T>
Implements
    [IDisposable](https://learn.microsoft.com/dotnet/api/system.idisposable), [IHostOperation](T_Tessa_Host_IHostOperation_1.htm)<T>
#### Параметры типа
T
     Тип контекста операции 
## __Конструкторы
[HostOperation<T>](M_Tessa_Host_HostOperation_1__ctor.htm)| Инициализирует
новый экземпляр класса HostOperation<T>  
---|---  
##  __Методы
[CheckDisposed](M_Tessa_Host_HostOperation_1_CheckDisposed.htm)|  Осуществляет
проверку вызван ли для объекта
[Dispose()](https://learn.microsoft.com/dotnet/api/system.idisposable.dispose#system-
idisposable-dispose) и в случае положительной проверки вызывает исключение
[ObjectDisposedException](https://learn.microsoft.com/dotnet/api/system.objectdisposedexception)  
---|---  
[Dispose](M_Tessa_Host_HostOperation_1_Dispose.htm)| Performs application-
defined tasks associated with freeing, releasing, or resetting unmanaged
resources.  
[Equals](https://learn.microsoft.com/dotnet/api/system.object.equals#system-
object-equals\(system-object\))| Determines whether the specified object is
equal to the current object.  
(Унаследован от
[Object](https://learn.microsoft.com/dotnet/api/system.object))  
[Execute](M_Tessa_Host_HostOperation_1_Execute.htm)|  Осуществляет выполнение
операции  
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
##  __Поля
[isDisposed](F_Tessa_Host_HostOperation_1_isDisposed.htm)|  Признак
уничтожения объекта  
---|---  
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
[Tessa.Host - пространство имён](N_Tessa_Host.htm)
