# CardType.TryGetCompletionOptionValidators - метод
Возвращает список валидаторов, связанных с вариантом завершения, подходящего
для заданной формы задания, или null, если текущий тип не является типом
задания, или с формой не связано ни одного или связано более одного варианта
завершения.
## __Definition
 **Пространство имён:** [Tessa.Cards](N_Tessa_Cards.htm)  
 **Сборка:** Tessa (в Tessa.dll) Версия: 3.6.0.17
C# __Копировать
     public SealableObjectList<CardTypeValidator> TryGetCompletionOptionValidators(
    	CardTypeForm form
    )
VB __Копировать
     Public Function TryGetCompletionOptionValidators ( 
    	form As CardTypeForm
    ) As SealableObjectList(Of CardTypeValidator)
C++ __Копировать
     public:
    SealableObjectList<CardTypeValidator^>^ TryGetCompletionOptionValidators(
    	CardTypeForm^ form
    )
F# __Копировать
     member TryGetCompletionOptionValidators : 
            form : CardTypeForm -> SealableObjectList<CardTypeValidator> 
#### Параметры
form [CardTypeForm](T_Tessa_Cards_CardTypeForm.htm)
    Форма задания, для которой требуется получить валидаторы.
#### Возвращаемое значение
[SealableObjectList](T_Tessa_Platform_Collections_SealableObjectList_1.htm)<[CardTypeValidator](T_Tessa_Cards_CardTypeValidator.htm)>  
Список валидаторов, связанных с вариантом завершения, подходящего для заданной
формы задания, или null, если текущий тип не является типом задания, или с
формой не связано ни одного или связано более одного варианта завершения.
## __См. также
#### Ссылки
[CardType - ](T_Tessa_Cards_CardType.htm)
[Tessa.Cards - пространство имён](N_Tessa_Cards.htm)
