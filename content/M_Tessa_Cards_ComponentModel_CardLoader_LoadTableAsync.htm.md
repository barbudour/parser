# CardLoader.LoadTableAsync - метод
Выполняет загрузку заданной физической коллекционной или древовидной секции
карточки, если её загрузка разрешена.
## __Definition
 **Пространство имён:**
[Tessa.Cards.ComponentModel](N_Tessa_Cards_ComponentModel.htm)  
 **Сборка:** Tessa (в Tessa.dll) Версия: 3.6.0.17
C# __Копировать
     public static Task LoadTableAsync(
    	CardGetContext context,
    	CardLoaderSectionInfo sectionInfo,
    	bool isHierarchy,
    	CancellationToken cancellationToken = default
    )
VB __Копировать
     Public Shared Function LoadTableAsync ( 
    	context As CardGetContext,
    	sectionInfo As CardLoaderSectionInfo,
    	isHierarchy As Boolean,
    	Optional cancellationToken As CancellationToken = Nothing
    ) As Task
C++ __Копировать
     public:
    static Task^ LoadTableAsync(
    	CardGetContext^ context, 
    	CardLoaderSectionInfo^ sectionInfo, 
    	bool isHierarchy, 
    	CancellationToken cancellationToken = CancellationToken()
    )
F# __Копировать
     static member LoadTableAsync : 
            context : CardGetContext * 
            sectionInfo : CardLoaderSectionInfo * 
            isHierarchy : bool * 
            ?cancellationToken : CancellationToken 
    (* Defaults:
            let _cancellationToken = defaultArg cancellationToken new CancellationToken()
    *)
    -> Task 
#### Параметры
context [CardGetContext](T_Tessa_Cards_ComponentModel_CardGetContext.htm)
    Контекст операции по загрузке карточки.
sectionInfo
[CardLoaderSectionInfo](T_Tessa_Cards_ComponentModel_CardLoaderSectionInfo.htm)
    Информация по загружаемой коллекционной или древовидной секции карточки.
isHierarchy [Boolean](https://learn.microsoft.com/dotnet/api/system.boolean)
    true, если загружаемая секция является древовидной; false, если загружаемая секция является коллекционной. 
cancellationToken
[CancellationToken](https://learn.microsoft.com/dotnet/api/system.threading.cancellationtoken)
(Optional)
    Объект, посредством которого можно отменить асинхронную задачу.
#### Возвращаемое значение
[Task](https://learn.microsoft.com/dotnet/api/system.threading.tasks.task)  
Асинхронная задача.
##  __См. также
#### Ссылки
[CardLoader - ](T_Tessa_Cards_ComponentModel_CardLoader.htm)
[Tessa.Cards.ComponentModel - пространство
имён](N_Tessa_Cards_ComponentModel.htm)
