# ICardGetFileContentExtensionContext.ContentFuncAsync - свойство
Функция, возвращающая поток с контентом файла. Используется только в случае,
если задано значение свойства
[Tessa.Cards.Extensions.ICardRequestExtensionContext{TRequest,TResponse}.Response].
Гарантируется, что для возвращаемого функцией значения будет вызван метод
[System.IDisposable.Dispose].
## __Definition
 **Пространство имён:** [Tessa.Cards.Extensions](N_Tessa_Cards_Extensions.htm)  
 **Сборка:** Tessa (в Tessa.dll) Версия: 3.6.0.17
C# __Копировать
    Func<CancellationToken, ValueTask<Stream>> ContentFuncAsync { get; set; }
VB __Копировать
     Property ContentFuncAsync As Func(Of CancellationToken, ValueTask(Of Stream))
    	Get
    	Set
C++ __Копировать
    property Func<CancellationToken, ValueTask<Stream^>>^ ContentFuncAsync {
    	Func<CancellationToken, ValueTask<Stream^>>^ get ();
    	void set (Func<CancellationToken, ValueTask<Stream^>>^ value);
    }
F# __Копировать
     abstract ContentFuncAsync : Func<CancellationToken, ValueTask<Stream>> with get, set
#### Значение свойства
[Func](https://learn.microsoft.com/dotnet/api/system.func-2)<[CancellationToken](https://learn.microsoft.com/dotnet/api/system.threading.cancellationtoken),
[ValueTask](https://learn.microsoft.com/dotnet/api/system.threading.tasks.valuetask-1)<[Stream](https://learn.microsoft.com/dotnet/api/system.io.stream)>>
##  __См. также
#### Ссылки
[ICardGetFileContentExtensionContext -
](T_Tessa_Cards_Extensions_ICardGetFileContentExtensionContext.htm)
[Tessa.Cards.Extensions - пространство имён](N_Tessa_Cards_Extensions.htm)
