# IExtensionExecutor<TExtension> \- интерфейс
Объект, выполняющий расширения заданного типа и определяющий время жизни
экземпляров расширений. Все методы объекта являются потокобезопасными.
## __Definition
 **Пространство имён:** [Tessa.Extensions](N_Tessa_Extensions.htm)  
 **Сборка:** Tessa (в Tessa.dll) Версия: 3.6.0.17
C# __Копировать
     public interface IExtensionExecutor<TExtension> : IAsyncDisposable
    where TExtension : class, IExtension
VB __Копировать
     Public Interface IExtensionExecutor(Of TExtension As {Class, IExtension})
    	Inherits IAsyncDisposable
C++ __Копировать
    generic<typename TExtension>
    where TExtension : ref class, IExtension
    public interface class IExtensionExecutor : IAsyncDisposable
F# __Копировать
     type IExtensionExecutor<'TExtension when 'TExtension : not struct and IExtension> = 
        interface
            interface IAsyncDisposable
        end
Implements
    [IAsyncDisposable](https://learn.microsoft.com/dotnet/api/system.iasyncdisposable)
#### Параметры типа
TExtension
    Тип расширений, выполняемых объектом.
##  __Заметки
Метод
[DisposeAsync()](https://learn.microsoft.com/dotnet/api/system.iasyncdisposable.disposeasync#system-
iasyncdisposable-disposeasync) выполняет очистку ресурсов, занимаемых каждым
из экземпляров расширений. Если все экземпляры не требуют специальной очистки,
то этот метод можно не вызывать.
## __Свойства
[IsFake](P_Tessa_Extensions_IExtensionExecutor_1_IsFake.htm)|  Признак того,
что объект не выполняет расширения, поскольку тип расширения не был
зарегистрирован.  
---|---  
## __Методы
[DisposeAsync](https://learn.microsoft.com/dotnet/api/system.iasyncdisposable.disposeasync#system-
iasyncdisposable-disposeasync)| Performs application-defined tasks associated
with freeing, releasing, or resetting unmanaged resources asynchronously.  
(Унаследован от
[IAsyncDisposable](https://learn.microsoft.com/dotnet/api/system.iasyncdisposable))  
---|---  
[ExecuteAsync<TContext>](M_Tessa_Extensions_IExtensionExecutor_1_ExecuteAsync__1.htm)|
Выполняет заданный метод асинхронно для всех зарегистрированных расширений
определённого типа.  
## __Методы расширения
[ExecuteWithExceptionCheckAsync<TExtension,
TExtensionContext>](M_Tessa_Platform_Runtime_RuntimeExtensions_ExecuteWithExceptionCheckAsync__2_1.htm)|
Выполняет заданный метод расширений с обработкой исключений, при возникновении
которых они обрабатываются объектом
[IMessageProvider](T_Tessa_Platform_Runtime_IMessageProvider.htm), например,
логируются и выводятся пользователю.  
(Определяется
[RuntimeExtensions](T_Tessa_Platform_Runtime_RuntimeExtensions.htm))  
---|---  
[ExecuteWithExceptionCheckAsync<TExtension,
TExtensionContext>](M_Tessa_Platform_Runtime_RuntimeExtensions_ExecuteWithExceptionCheckAsync__2.htm)|
Выполняет заданный метод расширений с обработкой исключений, при возникновении
которых они логируются объектом Logger.  
(Определяется
[RuntimeExtensions](T_Tessa_Platform_Runtime_RuntimeExtensions.htm))  
[ExecuteWithExceptionCheckAsync<TExtension,
TExtensionContext>](M_Tessa_UI_UIExtensions_ExecuteWithExceptionCheckAsync__2.htm)|
Выполняет заданный метод расширений с обработкой исключений, при возникновении
которых они логируются и выводятся пользователю.  
(Определяется [UIExtensions](T_Tessa_UI_UIExtensions.htm))  
##  __См. также
#### Ссылки
[Tessa.Extensions - пространство имён](N_Tessa_Extensions.htm)
