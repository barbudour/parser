# ILimitedPoolItem<T> \- интерфейс
Объект в пуле
[ILimitedPool<T>](T_Tessa_Platform_Collections_ILimitedPool_1.htm), время
жизни которого ограничено.
## __Definition
 **Пространство имён:**
[Tessa.Platform.Collections](N_Tessa_Platform_Collections.htm)  
 **Сборка:** Tessa (в Tessa.dll) Версия: 3.6.0.17
C# __Копировать
     public interface ILimitedPoolItem<out T> : IAsyncDisposable
VB __Копировать
     Public Interface ILimitedPoolItem(Of Out T)
    	Inherits IAsyncDisposable
C++ __Копировать
    generic<typename T>
    public interface class ILimitedPoolItem : IAsyncDisposable
F# __Копировать
     type ILimitedPoolItem<'T> = 
        interface
            interface IAsyncDisposable
        end
Implements
    [IAsyncDisposable](https://learn.microsoft.com/dotnet/api/system.iasyncdisposable)
#### Параметры типа
T
    Тип значения объекта в пуле.
##  __Свойства
[IsExpired](P_Tessa_Platform_Collections_ILimitedPoolItem_1_IsExpired.htm)|
Признак того, что время жизни объекта истекло, и после возврата в пул объект
должен быть пересоздан. Значение свойства определяется динамически в момент
обращения. Экземпляр объекта может быть не освобождён по завершению времени
жизни, если это не запрошено пулом
[ILimitedPool<T>](T_Tessa_Platform_Collections_ILimitedPool_1.htm), но
гарантируется, что такой объект не будет использован при запросе нового
объекта из пула.  
---|---  
[Value](P_Tessa_Platform_Collections_ILimitedPoolItem_1_Value.htm)|  Значение
объекта в пуле.  
## __Методы
[DisposeAsync](https://learn.microsoft.com/dotnet/api/system.iasyncdisposable.disposeasync#system-
iasyncdisposable-disposeasync)| Performs application-defined tasks associated
with freeing, releasing, or resetting unmanaged resources asynchronously.  
(Унаследован от
[IAsyncDisposable](https://learn.microsoft.com/dotnet/api/system.iasyncdisposable))  
---|---  
[Expire](M_Tessa_Platform_Collections_ILimitedPoolItem_1_Expire.htm)|
Указывает, что время жизни объекта истекло, даже если в действительности оно
ещё не истекло.  
## __См. также
#### Ссылки
[Tessa.Platform.Collections - пространство
имён](N_Tessa_Platform_Collections.htm)
