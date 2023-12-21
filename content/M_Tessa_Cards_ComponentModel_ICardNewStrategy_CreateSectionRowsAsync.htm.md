# ICardNewStrategy.CreateSectionRowsAsync - метод
Создаёт пустые строки коллекционных или древовидных секций создаваемой
карточки, доступные по имени секции.
## __Definition
 **Пространство имён:**
[Tessa.Cards.ComponentModel](N_Tessa_Cards_ComponentModel.htm)  
 **Сборка:** Tessa (в Tessa.dll) Версия: 3.6.0.17
C# __Копировать
    ValueTask<StringDictionaryStorage<CardRow>> CreateSectionRowsAsync(
    	CardNewContext context,
    	CancellationToken cancellationToken = default
    )
VB __Копировать
     Function CreateSectionRowsAsync ( 
    	context As CardNewContext,
    	Optional cancellationToken As CancellationToken = Nothing
    ) As ValueTask(Of StringDictionaryStorage(Of CardRow))
C++ __Копировать
    ValueTask<StringDictionaryStorage<CardRow^>^> CreateSectionRowsAsync(
    	CardNewContext^ context, 
    	CancellationToken cancellationToken = CancellationToken()
    )
F# __Копировать
     abstract CreateSectionRowsAsync : 
            context : CardNewContext * 
            ?cancellationToken : CancellationToken 
    (* Defaults:
            let _cancellationToken = defaultArg cancellationToken new CancellationToken()
    *)
    -> ValueTask<StringDictionaryStorage<CardRow>> 
#### Параметры
context [CardNewContext](T_Tessa_Cards_ComponentModel_CardNewContext.htm)
    Контекст операции по созданию карточки.
cancellationToken
[CancellationToken](https://learn.microsoft.com/dotnet/api/system.threading.cancellationtoken)
(Optional)
    Объект, посредством которого можно отменить асинхронную задачу.
#### Возвращаемое значение
[ValueTask](https://learn.microsoft.com/dotnet/api/system.threading.tasks.valuetask-1)<[StringDictionaryStorage](T_Tessa_Platform_Storage_StringDictionaryStorage_1.htm)<[CardRow](T_Tessa_Cards_CardRow.htm)>>  
Пустые строки коллекционных или древовидных секций создаваемой карточки,
доступные по имени секции.
## __См. также
#### Ссылки
[ICardNewStrategy - ](T_Tessa_Cards_ComponentModel_ICardNewStrategy.htm)
[Tessa.Cards.ComponentModel - пространство
имён](N_Tessa_Cards_ComponentModel.htm)
