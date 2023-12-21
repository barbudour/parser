# IExtensionExecutor<TExtension> \- методы
##  __Методы
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
[IExtensionExecutor<TExtension> \-
](T_Tessa_Extensions_IExtensionExecutor_1.htm)
[Tessa.Extensions - пространство имён](N_Tessa_Extensions.htm)
