# ParsedCard.FileStreams - свойство
##  __Definition
 **Пространство имён:** [Tessa.Cards](N_Tessa_Cards.htm)  
 **Сборка:** Tessa (в Tessa.dll) Версия: 3.6.0.17
C# __Копировать
     public IReadOnlyCollection<Func<CancellationToken, ValueTask<Stream>>> FileStreams { get; set; }
VB __Копировать
     Public Property FileStreams As IReadOnlyCollection(Of Func(Of CancellationToken, ValueTask(Of Stream)))
    	Get
    	Set
C++ __Копировать
     public:
    property IReadOnlyCollection<Func<CancellationToken, ValueTask<Stream^>>^>^ FileStreams {
    	IReadOnlyCollection<Func<CancellationToken, ValueTask<Stream^>>^>^ get ();
    	void set (IReadOnlyCollection<Func<CancellationToken, ValueTask<Stream^>>^>^ value);
    }
F# __Копировать
     member FileStreams : IReadOnlyCollection<Func<CancellationToken, ValueTask<Stream>>> with get, set
#### Значение свойства
[IReadOnlyCollection](https://learn.microsoft.com/dotnet/api/system.collections.generic.ireadonlycollection-1)<[Func](https://learn.microsoft.com/dotnet/api/system.func-2)<[CancellationToken](https://learn.microsoft.com/dotnet/api/system.threading.cancellationtoken),
[ValueTask](https://learn.microsoft.com/dotnet/api/system.threading.tasks.valuetask-1)<[Stream](https://learn.microsoft.com/dotnet/api/system.io.stream)>>>
##  __См. также
#### Ссылки
[ParsedCard - ](T_Tessa_Cards_ParsedCard.htm)
[Tessa.Cards - пространство имён](N_Tessa_Cards.htm)
