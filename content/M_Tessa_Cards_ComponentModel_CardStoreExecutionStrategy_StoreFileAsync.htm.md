# CardStoreExecutionStrategy.StoreFileAsync - метод
Выполняет сохранение файла.
##  __Definition
 **Пространство имён:**
[Tessa.Cards.ComponentModel](N_Tessa_Cards_ComponentModel.htm)  
 **Сборка:** Tessa (в Tessa.dll) Версия: 3.6.0.17
C# __Копировать
     public Task StoreFileAsync(
    	CardStoreContext context,
    	CardFile file
    )
VB __Копировать
     Public Function StoreFileAsync ( 
    	context As CardStoreContext,
    	file As CardFile
    ) As Task
C++ __Копировать
     public:
    virtual Task^ StoreFileAsync(
    	CardStoreContext^ context, 
    	CardFile^ file
    ) sealed
F# __Копировать
     abstract StoreFileAsync : 
            context : CardStoreContext * 
            file : CardFile -> Task 
    override StoreFileAsync : 
            context : CardStoreContext * 
            file : CardFile -> Task 
#### Параметры
context [CardStoreContext](T_Tessa_Cards_ComponentModel_CardStoreContext.htm)
    Контекст операции по сохранению карточки, к которой прикреплён файл.
file [CardFile](T_Tessa_Cards_CardFile.htm)
    Сохраняемый файл.
#### Возвращаемое значение
[Task](https://learn.microsoft.com/dotnet/api/system.threading.tasks.task)  
Асинхронная задача.
#### Реализации
[ICardStoreExecutionStrategy.StoreFileAsync(CardStoreContext,
CardFile)](M_Tessa_Cards_ComponentModel_ICardStoreExecutionStrategy_StoreFileAsync.htm)  
##  __См. также
#### Ссылки
[CardStoreExecutionStrategy -
](T_Tessa_Cards_ComponentModel_CardStoreExecutionStrategy.htm)
[Tessa.Cards.ComponentModel - пространство
имён](N_Tessa_Cards_ComponentModel.htm)
