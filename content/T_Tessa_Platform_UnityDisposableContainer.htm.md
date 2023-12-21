# UnityDisposableContainer - класс
Контейнер, содержащий объекты
[IDisposable](https://learn.microsoft.com/dotnet/api/system.idisposable),
которые будут освобождены при закрытии контейнеров IUnityContainer.
## __Definition
 **Пространство имён:** [Tessa.Platform](N_Tessa_Platform.htm)  
 **Сборка:** Tessa (в Tessa.dll) Версия: 3.6.0.17
C# __Копировать
     public sealed class UnityDisposableContainer : IUnityDisposableContainer
VB __Копировать
     Public NotInheritable Class UnityDisposableContainer
    	Implements IUnityDisposableContainer
C++ __Копировать
     public ref class UnityDisposableContainer sealed : IUnityDisposableContainer
F# __Копировать
     [<SealedAttribute>]
    type UnityDisposableContainer = 
        class
            interface IUnityDisposableContainer
        end
Inheritance
    [Object](https://learn.microsoft.com/dotnet/api/system.object) __ UnityDisposableContainer
Implements
    [IUnityDisposableContainer](T_Tessa_Platform_IUnityDisposableContainer.htm)
##  __Конструкторы
[UnityDisposableContainer](M_Tessa_Platform_UnityDisposableContainer__ctor.htm)|
Инициализирует новый экземпляр класса UnityDisposableContainer  
---|---  
##  __Методы
[DisposeAllAsync](M_Tessa_Platform_UnityDisposableContainer_DisposeAllAsync.htm)|
Освобождает все экземпляры
[IDisposable](https://learn.microsoft.com/dotnet/api/system.idisposable) и
[IAsyncDisposable](https://learn.microsoft.com/dotnet/api/system.iasyncdisposable),
которые были зарегистрированы в текущем объекте, в порядке, обратном
регистрации. После вызова невозможны дополнительные регистрации.  
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
[Register(IAsyncDisposable)](M_Tessa_Platform_UnityDisposableContainer_Register.htm)|
Регистрирует заданный экземпляр
[IAsyncDisposable](https://learn.microsoft.com/dotnet/api/system.iasyncdisposable),
чтобы его метод
[DisposeAsync()](https://learn.microsoft.com/dotnet/api/system.iasyncdisposable.disposeasync#system-
iasyncdisposable-disposeasync) был вызван при освобождении контейнера методом
[DisposeAllAsync()](M_Tessa_Platform_IUnityDisposableContainer_DisposeAllAsync.htm).
Возвращает true, если объект был зарегистрирован, или false, если объект не
может быть зарегистрирован, т.к. все объекты уже были освобождены.  
[Register(IDisposable)](M_Tessa_Platform_UnityDisposableContainer_Register_1.htm)|
Регистрирует заданный экземпляр
[IDisposable](https://learn.microsoft.com/dotnet/api/system.idisposable),
чтобы его метод
[Dispose()](https://learn.microsoft.com/dotnet/api/system.idisposable.dispose#system-
idisposable-dispose) был вызван при освобождении контейнера методом
[DisposeAllAsync()](M_Tessa_Platform_IUnityDisposableContainer_DisposeAllAsync.htm).
Возвращает true, если объект был зарегистрирован, или false, если объект не
может быть зарегистрирован, т.к. все объекты уже были освобождены.  
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
[Tessa.Platform - пространство имён](N_Tessa_Platform.htm)
