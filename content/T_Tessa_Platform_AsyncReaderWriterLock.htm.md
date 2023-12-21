# AsyncReaderWriterLock - класс
Объект, обеспечивающий блокировки на чтение и запись. Объект можно получить из
Unity как PerResolve зависимость.
## __Definition
 **Пространство имён:** [Tessa.Platform](N_Tessa_Platform.htm)  
 **Сборка:** Tessa (в Tessa.dll) Версия: 3.6.0.17
C# __Копировать
     public sealed class AsyncReaderWriterLock : IAsyncReaderWriterLock
VB __Копировать
     Public NotInheritable Class AsyncReaderWriterLock
    	Implements IAsyncReaderWriterLock
C++ __Копировать
     public ref class AsyncReaderWriterLock sealed : IAsyncReaderWriterLock
F# __Копировать
     [<SealedAttribute>]
    type AsyncReaderWriterLock = 
        class
            interface IAsyncReaderWriterLock
        end
Inheritance
    [Object](https://learn.microsoft.com/dotnet/api/system.object) __ AsyncReaderWriterLock
Implements
    [IAsyncReaderWriterLock](T_Tessa_Platform_IAsyncReaderWriterLock.htm)
##  __Конструкторы
[AsyncReaderWriterLock](M_Tessa_Platform_AsyncReaderWriterLock__ctor.htm)|
Создаёт экземпляр класса по умолчанию.  
---|---  
## __Методы
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
[MemberwiseClone](https://learn.microsoft.com/dotnet/api/system.object.memberwiseclone#system-
object-memberwiseclone)| Creates a shallow copy of the current
[Object](https://learn.microsoft.com/dotnet/api/system.object).  
(Унаследован от
[Object](https://learn.microsoft.com/dotnet/api/system.object))  
[ReaderLockAsync](M_Tessa_Platform_AsyncReaderWriterLock_ReaderLockAsync.htm)|
Выполняет взятие блокировки на чтение. Ожидает освобождения блокировки на
запись, если она была взята. Внимание! Не вызывайте метод
[Dispose()](https://learn.microsoft.com/dotnet/api/system.idisposable.dispose#system-
idisposable-dispose) у возвращённого объекта более одного раза. Рекомендуется
использовать конструкцию using и не обращаться к возвращаемому объекту
[IDisposable](https://learn.microsoft.com/dotnet/api/system.idisposable)
другим образом.  
[ToString](https://learn.microsoft.com/dotnet/api/system.object.tostring#system-
object-tostring)| Returns a string that represents the current object.  
(Унаследован от
[Object](https://learn.microsoft.com/dotnet/api/system.object))  
[WriterLockAsync](M_Tessa_Platform_AsyncReaderWriterLock_WriterLockAsync.htm)|
Выполняет взятие эксклюзивной блокировки на запись. Ожидает освобождения всех
блокировок на чтение или параллельной блокировки на запись, если они были
взяты. Внимание! Не вызывайте метод
[Dispose()](https://learn.microsoft.com/dotnet/api/system.idisposable.dispose#system-
idisposable-dispose) у возвращённого объекта более одного раза. Рекомендуется
использовать конструкцию using и не обращаться к возвращаемому объекту
[IDisposable](https://learn.microsoft.com/dotnet/api/system.idisposable)
другим образом.  
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
[Tessa.Platform - пространство имён](N_Tessa_Platform.htm)
