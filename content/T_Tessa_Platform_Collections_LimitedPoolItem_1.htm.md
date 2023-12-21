# LimitedPoolItem<T> \- класс
Объект в пуле
[ILimitedPool<T>](T_Tessa_Platform_Collections_ILimitedPool_1.htm), время
жизни которого ограничено.
## __Definition
 **Пространство имён:**
[Tessa.Platform.Collections](N_Tessa_Platform_Collections.htm)  
 **Сборка:** Tessa (в Tessa.dll) Версия: 3.6.0.17
C# __Копировать
     public sealed class LimitedPoolItem<T> : ILimitedPoolItem<T>, 
    	IAsyncDisposable
VB __Копировать
     Public NotInheritable Class LimitedPoolItem(Of T)
    	Implements ILimitedPoolItem(Of T), IAsyncDisposable
C++ __Копировать
    generic<typename T>
    public ref class LimitedPoolItem sealed : ILimitedPoolItem<T>, 
    	IAsyncDisposable
F# __Копировать
     [<SealedAttribute>]
    type LimitedPoolItem<'T> = 
        class
            interface ILimitedPoolItem<'T>
            interface IAsyncDisposable
        end
Inheritance
    [Object](https://learn.microsoft.com/dotnet/api/system.object) __ LimitedPoolItem<T>
Implements
    [IAsyncDisposable](https://learn.microsoft.com/dotnet/api/system.iasyncdisposable), [ILimitedPoolItem](T_Tessa_Platform_Collections_ILimitedPoolItem_1.htm)<T>
#### Параметры типа
T
    Тип значения объекта в пуле.
##  __Конструкторы
[LimitedPoolItem<T>](M_Tessa_Platform_Collections_LimitedPoolItem_1__ctor.htm)|
Создаёт экземпляр класса с указанием значения объекта в пуле и параметров его
жизненного цикла.  
---|---  
## __Свойства
[IsExpired](P_Tessa_Platform_Collections_LimitedPoolItem_1_IsExpired.htm)|
Признак того, что время жизни объекта истекло, и после возврата в пул объект
должен быть пересоздан. Значение свойства определяется динамически в момент
обращения. Экземпляр объекта может быть не освобождён по завершению времени
жизни, если это не запрошено пулом
[ILimitedPool<T>](T_Tessa_Platform_Collections_ILimitedPool_1.htm), но
гарантируется, что такой объект не будет использован при запросе нового
объекта из пула.  
---|---  
[Value](P_Tessa_Platform_Collections_LimitedPoolItem_1_Value.htm)|  Значение
объекта в пуле.  
## __Методы
[DisposeAsync](M_Tessa_Platform_Collections_LimitedPoolItem_1_DisposeAsync.htm)|
Освобождает ресурсы, занимаемые объектом.  
---|---  
[Equals](https://learn.microsoft.com/dotnet/api/system.object.equals#system-
object-equals\(system-object\))| Determines whether the specified object is
equal to the current object.  
(Унаследован от
[Object](https://learn.microsoft.com/dotnet/api/system.object))  
[Expire](M_Tessa_Platform_Collections_LimitedPoolItem_1_Expire.htm)|
Указывает, что время жизни объекта истекло, даже если в действительности оно
ещё не истекло.  
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
[Tessa.Platform.Collections - пространство
имён](N_Tessa_Platform_Collections.htm)
