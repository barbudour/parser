# CardFileSourceOverride.Apply - метод
Применяет изменения для указанного объекта, и возвращает его изменённую копию.
## __Definition
 **Пространство имён:** [Tessa.Cards](N_Tessa_Cards.htm)  
 **Сборка:** Tessa (в Tessa.dll) Версия: 3.6.0.17
C# __Копировать
     public ICardFileSource Apply(
    	ICardFileSource source
    )
VB __Копировать
     Public Function Apply ( 
    	source As ICardFileSource
    ) As ICardFileSource
C++ __Копировать
     public:
    virtual ICardFileSource^ Apply(
    	ICardFileSource^ source
    ) sealed
F# __Копировать
     abstract Apply : 
            source : ICardFileSource -> ICardFileSource 
    override Apply : 
            source : ICardFileSource -> ICardFileSource 
#### Параметры
source [ICardFileSource](T_Tessa_Cards_ICardFileSource.htm)
    Объект, свойства которого переопределяются.
#### Возвращаемое значение
[ICardFileSource](T_Tessa_Cards_ICardFileSource.htm)  
Объект с переопределёнными свойствами.
#### Реализации
[ICardFileSourceOverride.Apply(ICardFileSource)](M_Tessa_Cards_ICardFileSourceOverride_Apply.htm)  
##  __См. также
#### Ссылки
[CardFileSourceOverride - ](T_Tessa_Cards_CardFileSourceOverride.htm)
[Tessa.Cards - пространство имён](N_Tessa_Cards.htm)
