# ICardControlAdditionalInfoRegistry.TryGetSourceInfoFunc - метод
Метод для получения кастомного метода получения информации об источнике данных
контрола.
## __Definition
 **Пространство имён:** [Tessa.Cards](N_Tessa_Cards.htm)  
 **Сборка:** Tessa (в Tessa.dll) Версия: 3.6.0.17
C# __Копировать
     CardControlSourceInfoDelegate TryGetSourceInfoFunc(
    	CardControlType controlType
    )
VB __Копировать
     Function TryGetSourceInfoFunc ( 
    	controlType As CardControlType
    ) As CardControlSourceInfoDelegate
C++ __Копировать
    CardControlSourceInfoDelegate^ TryGetSourceInfoFunc(
    	CardControlType^ controlType
    )
F# __Копировать
     abstract TryGetSourceInfoFunc : 
            controlType : CardControlType -> CardControlSourceInfoDelegate 
#### Параметры
controlType [CardControlType](T_Tessa_Cards_CardControlType.htm)
    Тип контрола
#### Возвращаемое значение
[CardControlSourceInfoDelegate](T_Tessa_Cards_CardControlSourceInfoDelegate.htm)  
Возвращает метод для получения кастомного метода получения информации об
источнике данных контрола, или null, если для контрола не было
зарегистрировано этого метода.
##  __См. также
#### Ссылки
[ICardControlAdditionalInfoRegistry -
](T_Tessa_Cards_ICardControlAdditionalInfoRegistry.htm)
[Tessa.Cards - пространство имён](N_Tessa_Cards.htm)
