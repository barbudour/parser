# ICardControlAdditionalInfoRegistry.RegisterSourceInfoFunc - метод
Метод для регистрации кастомного метода получения информации об источнике
данных контрола.
## __Definition
 **Пространство имён:** [Tessa.Cards](N_Tessa_Cards.htm)  
 **Сборка:** Tessa (в Tessa.dll) Версия: 3.6.0.17
C# __Копировать
     ICardControlAdditionalInfoRegistry RegisterSourceInfoFunc(
    	CardControlType controlType,
    	CardControlSourceInfoDelegate func
    )
VB __Копировать
     Function RegisterSourceInfoFunc ( 
    	controlType As CardControlType,
    	func As CardControlSourceInfoDelegate
    ) As ICardControlAdditionalInfoRegistry
C++ __Копировать
    ICardControlAdditionalInfoRegistry^ RegisterSourceInfoFunc(
    	CardControlType^ controlType, 
    	CardControlSourceInfoDelegate^ func
    )
F# __Копировать
     abstract RegisterSourceInfoFunc : 
            controlType : CardControlType * 
            func : CardControlSourceInfoDelegate -> ICardControlAdditionalInfoRegistry 
#### Параметры
controlType [CardControlType](T_Tessa_Cards_CardControlType.htm)
    Тип контрола
func
[CardControlSourceInfoDelegate](T_Tessa_Cards_CardControlSourceInfoDelegate.htm)
    Метод для получения информации об источнике данных контрола
#### Возвращаемое значение
[ICardControlAdditionalInfoRegistry](T_Tessa_Cards_ICardControlAdditionalInfoRegistry.htm)  
Возвращает текущий экземпляр реестра элементов управоения
##  __См. также
#### Ссылки
[ICardControlAdditionalInfoRegistry -
](T_Tessa_Cards_ICardControlAdditionalInfoRegistry.htm)
[Tessa.Cards - пространство имён](N_Tessa_Cards.htm)
