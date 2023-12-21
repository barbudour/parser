# CardSchemeInfoProvider(ICardSchemeInfoProvider, CardType) - конструктор
Создаёт экземпляр класса с указанием объекта
[ICardSchemeInfoProvider](T_Tessa_Cards_ICardSchemeInfoProvider.htm).
## __Definition
 **Пространство имён:** [Tessa.Cards](N_Tessa_Cards.htm)  
 **Сборка:** Tessa (в Tessa.dll) Версия: 3.6.0.17
C# __Копировать
     public CardSchemeInfoProvider(
    	ICardSchemeInfoProvider schemeInfoProvider,
    	CardType cardType = null
    )
VB __Копировать
     Public Sub New ( 
    	schemeInfoProvider As ICardSchemeInfoProvider,
    	Optional cardType As CardType = Nothing
    )
C++ __Копировать
     public:
    CardSchemeInfoProvider(
    	ICardSchemeInfoProvider^ schemeInfoProvider, 
    	CardType^ cardType = nullptr
    )
F# __Копировать
     new : 
            schemeInfoProvider : ICardSchemeInfoProvider * 
            ?cardType : CardType 
    (* Defaults:
            let _cardType = defaultArg cardType null
    *)
    -> CardSchemeInfoProvider
#### Параметры
schemeInfoProvider
[ICardSchemeInfoProvider](T_Tessa_Cards_ICardSchemeInfoProvider.htm)
     Объект, используемый для получения информации по таблицам. При сбрасывании кэша в текущем объекте, он также сбрасывается и в переданном. 
cardType [CardType](T_Tessa_Cards_CardType.htm) (Optional)
     Тип карточки, для которого создаётся объект, или null, если объект будет возвращать информацию по таблицам для всех типов карточек. 
## __См. также
#### Ссылки
[CardSchemeInfoProvider - ](T_Tessa_Cards_CardSchemeInfoProvider.htm)
[CardSchemeInfoProvider -
перегрузка](Overload_Tessa_Cards_CardSchemeInfoProvider__ctor.htm)
[Tessa.Cards - пространство имён](N_Tessa_Cards.htm)
