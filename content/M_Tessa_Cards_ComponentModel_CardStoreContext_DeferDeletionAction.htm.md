# CardStoreContext.DeferDeletionAction - метод
Откладывает выполнение действия по удалению элемента карточки.
## __Definition
 **Пространство имён:**
[Tessa.Cards.ComponentModel](N_Tessa_Cards_ComponentModel.htm)  
 **Сборка:** Tessa (в Tessa.dll) Версия: 3.6.0.17
C# __Копировать
     public void DeferDeletionAction(
    	Func<CardStoreContext, Task> actionAsync
    )
VB __Копировать
     Public Sub DeferDeletionAction ( 
    	actionAsync As Func(Of CardStoreContext, Task)
    )
C++ __Копировать
     public:
    void DeferDeletionAction(
    	Func<CardStoreContext^, Task^>^ actionAsync
    )
F# __Копировать
     member DeferDeletionAction : 
            actionAsync : Func<CardStoreContext, Task> -> unit 
#### Параметры
actionAsync
[Func](https://learn.microsoft.com/dotnet/api/system.func-2)<[CardStoreContext](T_Tessa_Cards_ComponentModel_CardStoreContext.htm),
[Task](https://learn.microsoft.com/dotnet/api/system.threading.tasks.task)>
     Действие по удалению элемента карточки, выполнение которого должно быть отложено. 
## __См. также
#### Ссылки
[CardStoreContext - ](T_Tessa_Cards_ComponentModel_CardStoreContext.htm)
[Tessa.Cards.ComponentModel - пространство
имён](N_Tessa_Cards_ComponentModel.htm)
