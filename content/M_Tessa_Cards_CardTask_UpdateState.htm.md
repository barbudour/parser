# CardTask.UpdateState - метод
Обновляет состояние задания [State](P_Tessa_Cards_CardTask_State.htm) и
действие с заданием [Action](P_Tessa_Cards_CardTask_Action.htm) в зависимости
от наличия изменений во флагах или в данных карточки задания.
## __Definition
 **Пространство имён:** [Tessa.Cards](N_Tessa_Cards.htm)  
 **Сборка:** Tessa (в Tessa.dll) Версия: 3.6.0.17
C# __Копировать
     public bool UpdateState()
VB __Копировать
     Public Function UpdateState As Boolean
C++ __Копировать
     public:
    bool UpdateState()
F# __Копировать
     member UpdateState : unit -> bool 
#### Возвращаемое значение
[Boolean](https://learn.microsoft.com/dotnet/api/system.boolean)  
true, если состояние задания было изменено; false, если состояние задания не
требуется изменять, т.к. изменения уже зафиксированы или отсуствуют.
## __См. также
#### Ссылки
[CardTask - ](T_Tessa_Cards_CardTask.htm)
[Tessa.Cards - пространство имён](N_Tessa_Cards.htm)
