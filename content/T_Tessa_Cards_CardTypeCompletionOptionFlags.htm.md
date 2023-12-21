# CardTypeCompletionOptionFlags - перечисление
Флаги варианта завершения в типе карточки задания.
## __Definition
 **Пространство имён:** [Tessa.Cards](N_Tessa_Cards.htm)  
 **Сборка:** Tessa (в Tessa.dll) Версия: 3.6.0.17
C# __Копировать
    [FlagsAttribute]
    public enum CardTypeCompletionOptionFlags
VB __Копировать
    <FlagsAttribute>
    Public Enumeration CardTypeCompletionOptionFlags
C++ __Копировать
    [FlagsAttribute]
    public enum class CardTypeCompletionOptionFlags
F# __Копировать
     [<FlagsAttribute>]
    type CardTypeCompletionOptionFlags
##  __Члены
None| 0|  Флаги отсутствуют.  
---|---|---  
Additional| 1|  Вариант завершения является дополнительным, т.е. он скрывается
из списка кнопок в задании и отображается под кнопкой с дополнительными
вариантами.  
DoNotDeleteTask| 2|  Вариант завершения не приводит к удалению задания, т.к.
считается изменением задания.  
ShowForAuthor| 4|  Вариант завершения доступен автору. Не влияет на
доступность пользователям в роли, на которую назначено задание. Если вариант
завершения должен быть доступен автору и скрыт от пользователей в роли, то
следует установить флаги ShowForAuthor и HideForPerformer. Если вариант
завершения доступен как автору, так и пользователям в роли, то следует
установить флаг ShowForAuthor и не устанавливать HideForPerformer.  
HideForPerformer| 8|  Вариант завершения скрыт от исполнителя, т.е. от
пользователей в роли, на которую назначено задание.  
## __См. также
#### Ссылки
[Tessa.Cards - пространство имён](N_Tessa_Cards.htm)
