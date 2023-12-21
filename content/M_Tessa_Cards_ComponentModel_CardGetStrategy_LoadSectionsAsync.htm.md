# CardGetStrategy.LoadSectionsAsync - метод
Загружает секции карточки.
##  __Definition
 **Пространство имён:**
[Tessa.Cards.ComponentModel](N_Tessa_Cards_ComponentModel.htm)  
 **Сборка:** Tessa (в Tessa.dll) Версия: 3.6.0.17
C# __Копировать
     public Task<bool> LoadSectionsAsync(
    	CardGetContext context,
    	CancellationToken cancellationToken = default
    )
VB __Копировать
     Public Function LoadSectionsAsync ( 
    	context As CardGetContext,
    	Optional cancellationToken As CancellationToken = Nothing
    ) As Task(Of Boolean)
C++ __Копировать
     public:
    virtual Task<bool>^ LoadSectionsAsync(
    	CardGetContext^ context, 
    	CancellationToken cancellationToken = CancellationToken()
    ) sealed
F# __Копировать
     abstract LoadSectionsAsync : 
            context : CardGetContext * 
            ?cancellationToken : CancellationToken 
    (* Defaults:
            let _cancellationToken = defaultArg cancellationToken new CancellationToken()
    *)
    -> Task<bool> 
    override LoadSectionsAsync : 
            context : CardGetContext * 
            ?cancellationToken : CancellationToken 
    (* Defaults:
            let _cancellationToken = defaultArg cancellationToken new CancellationToken()
    *)
    -> Task<bool> 
#### Параметры
context [CardGetContext](T_Tessa_Cards_ComponentModel_CardGetContext.htm)
    Контекст операции по загрузке карточки.
cancellationToken
[CancellationToken](https://learn.microsoft.com/dotnet/api/system.threading.cancellationtoken)
(Optional)
    Объект, посредством которого можно отменить асинхронную задачу.
#### Возвращаемое значение
[Task](https://learn.microsoft.com/dotnet/api/system.threading.tasks.task-1)<[Boolean](https://learn.microsoft.com/dotnet/api/system.boolean)>  
true, если секции карточки были успешно загружены; false в противном случае.
#### Реализации
[ICardGetStrategy.LoadSectionsAsync(CardGetContext,
CancellationToken)](M_Tessa_Cards_ComponentModel_ICardGetStrategy_LoadSectionsAsync.htm)  
##  __См. также
#### Ссылки
[CardGetStrategy - ](T_Tessa_Cards_ComponentModel_CardGetStrategy.htm)
[Tessa.Cards.ComponentModel - пространство
имён](N_Tessa_Cards_ComponentModel.htm)
