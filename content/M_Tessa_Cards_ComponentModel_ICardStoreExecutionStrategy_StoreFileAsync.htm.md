# ICardStoreExecutionStrategy.StoreFileAsync - метод
Выполняет сохранение файла.
##  __Definition
 **Пространство имён:**
[Tessa.Cards.ComponentModel](N_Tessa_Cards_ComponentModel.htm)  
 **Сборка:** Tessa (в Tessa.dll) Версия: 3.6.0.17
C# __Копировать
     Task StoreFileAsync(
    	CardStoreContext context,
    	CardFile file
    )
VB __Копировать
     Function StoreFileAsync ( 
    	context As CardStoreContext,
    	file As CardFile
    ) As Task
C++ __Копировать
    Task^ StoreFileAsync(
    	CardStoreContext^ context, 
    	CardFile^ file
    )
F# __Копировать
     abstract StoreFileAsync : 
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
##  __См. также
#### Ссылки
[ICardStoreExecutionStrategy -
](T_Tessa_Cards_ComponentModel_ICardStoreExecutionStrategy.htm)
[Tessa.Cards.ComponentModel - пространство
имён](N_Tessa_Cards_ComponentModel.htm)
