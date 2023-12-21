# CardStoreContext.CreateForAsync - метод
Создаёт контекст операции по сохранению карточки, которая вложена в текущую
карточку. Это может быть карточка файла или задания.
## __Definition
 **Пространство имён:**
[Tessa.Cards.ComponentModel](N_Tessa_Cards_ComponentModel.htm)  
 **Сборка:** Tessa (в Tessa.dll) Версия: 3.6.0.17
C# __Копировать
     public ValueTask<CardStoreContext> CreateForAsync(
    	Card card,
    	CardType cardType,
    	CardStoreMode storeMode,
    	CardStoreMethod storeMethod,
    	bool repairSections,
    	CancellationToken cancellationToken = default
    )
VB __Копировать
     Public Function CreateForAsync ( 
    	card As Card,
    	cardType As CardType,
    	storeMode As CardStoreMode,
    	storeMethod As CardStoreMethod,
    	repairSections As Boolean,
    	Optional cancellationToken As CancellationToken = Nothing
    ) As ValueTask(Of CardStoreContext)
C++ __Копировать
     public:
    ValueTask<CardStoreContext^> CreateForAsync(
    	Card^ card, 
    	CardType^ cardType, 
    	CardStoreMode storeMode, 
    	CardStoreMethod storeMethod, 
    	bool repairSections, 
    	CancellationToken cancellationToken = CancellationToken()
    )
F# __Копировать
     member CreateForAsync : 
            card : Card * 
            cardType : CardType * 
            storeMode : CardStoreMode * 
            storeMethod : CardStoreMethod * 
            repairSections : bool * 
            ?cancellationToken : CancellationToken 
    (* Defaults:
            let _cancellationToken = defaultArg cancellationToken new CancellationToken()
    *)
    -> ValueTask<CardStoreContext> 
#### Параметры
card [Card](T_Tessa_Cards_Card.htm)
     Карточка файла или задания, которую требуется сохранить. Она должна быть вложена в текущую карточку. 
cardType [CardType](T_Tessa_Cards_CardType.htm)
    Тип вложенной карточки, которую требуется сохранить.
storeMode [CardStoreMode](T_Tessa_Cards_CardStoreMode.htm)
    Способ сохранения вложенной карточки.
storeMethod [CardStoreMethod](T_Tessa_Cards_CardStoreMethod.htm)
    Специализация для способа сохранения вложенной карточки.
repairSections
[Boolean](https://learn.microsoft.com/dotnet/api/system.boolean)
    Флаг указывает на то, что нужно починить (добавить) строковые секции карточки в случае, если они отсутствуют в БД.
cancellationToken
[CancellationToken](https://learn.microsoft.com/dotnet/api/system.threading.cancellationtoken)
(Optional)
    Объект, посредством которого можно отменить асинхронную задачу.
#### Возвращаемое значение
[ValueTask](https://learn.microsoft.com/dotnet/api/system.threading.tasks.valuetask-1)<[CardStoreContext](T_Tessa_Cards_ComponentModel_CardStoreContext.htm)>  
Контекст операции по сохранению карточки, которая вложена в текущую карточку.
##  __См. также
#### Ссылки
[CardStoreContext - ](T_Tessa_Cards_ComponentModel_CardStoreContext.htm)
[Tessa.Cards.ComponentModel - пространство
имён](N_Tessa_Cards_ComponentModel.htm)
