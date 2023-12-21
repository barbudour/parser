# CardTypeTabControl.EqualsInternal - метод
Сравнивает заданный объект с текущим по всем полям.
##  __Definition
 **Пространство имён:** [Tessa.Cards](N_Tessa_Cards.htm)  
 **Сборка:** Tessa (в Tessa.dll) Версия: 3.6.0.17
C# __Копировать
     protected override bool EqualsInternal(
    	CardTypeContent other
    )
VB __Копировать
     Protected Overrides Function EqualsInternal ( 
    	other As CardTypeContent
    ) As Boolean
C++ __Копировать
     protected:
    virtual bool EqualsInternal(
    	CardTypeContent^ other
    ) override
F# __Копировать
     abstract EqualsInternal : 
            other : CardTypeContent -> bool 
    override EqualsInternal : 
            other : CardTypeContent -> bool 
#### Параметры
other [CardTypeContent](T_Tessa_Cards_CardTypeContent.htm)
     Объект, с которым производится сравнение. Он не равен null, и его тип совпадает с типом текущего объекта. 
#### Возвращаемое значение
[Boolean](https://learn.microsoft.com/dotnet/api/system.boolean)  
true, если объекты равны; false в противном случае.
## __См. также
#### Ссылки
[CardTypeTabControl - ](T_Tessa_Cards_CardTypeTabControl.htm)
[Tessa.Cards - пространство имён](N_Tessa_Cards.htm)
