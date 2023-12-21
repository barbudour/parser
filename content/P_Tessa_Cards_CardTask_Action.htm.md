# CardTask.Action - свойство
Действие, выполняемое для задания. По умолчанию имеет значение Create.
## __Definition
 **Пространство имён:** [Tessa.Cards](N_Tessa_Cards.htm)  
 **Сборка:** Tessa (в Tessa.dll) Версия: 3.6.0.17
C# __Копировать
     public CardTaskAction Action { get; set; }
VB __Копировать
     Public Property Action As CardTaskAction
    	Get
    	Set
C++ __Копировать
     public:
    property CardTaskAction Action {
    	CardTaskAction get ();
    	void set (CardTaskAction value);
    }
F# __Копировать
     member Action : CardTaskAction with get, set
#### Значение свойства
[CardTaskAction](T_Tessa_Cards_CardTaskAction.htm)
##  __Заметки
Если задание создаётся действием Progress, а не Create, то оно автоматически
берётся в работу.
## __См. также
#### Ссылки
[CardTask - ](T_Tessa_Cards_CardTask.htm)
[Tessa.Cards - пространство имён](N_Tessa_Cards.htm)
