# ICardTypeVisitor - интерфейс
Выполняет посещение объектов типа карточки.
## __Definition
 **Пространство имён:** [Tessa.Cards](N_Tessa_Cards.htm)  
 **Сборка:** Tessa (в Tessa.dll) Версия: 3.6.0.17
C# __Копировать
     public interface ICardTypeVisitor
VB __Копировать
     Public Interface ICardTypeVisitor
C++ __Копировать
     public interface class ICardTypeVisitor
F# __Копировать
     type ICardTypeVisitor = interface end
##  __Методы
[BuildResultAsync](M_Tessa_Cards_ICardTypeVisitor_BuildResultAsync.htm)|
Возвращает результат валидации, полученный посредством посещения объектов типа
карточки.  
---|---  
[VisitBlockAsync](M_Tessa_Cards_ICardTypeVisitor_VisitBlockAsync.htm)|
Посещает объект [Tessa.Cards.CardTypeBlock] в типе карточки.  
[VisitColumnAsync](M_Tessa_Cards_ICardTypeVisitor_VisitColumnAsync.htm)|
Посещает объект [Tessa.Cards.CardTypeColumn] в типе карточки.  
[VisitCompletionOptionAsync](M_Tessa_Cards_ICardTypeVisitor_VisitCompletionOptionAsync.htm)|
Посещает объект [Tessa.Cards.CardTypeCompletionOption] в типе карточки.  
[VisitControlAsync](M_Tessa_Cards_ICardTypeVisitor_VisitControlAsync.htm)|
Посещает объект [Tessa.Cards.CardTypeControl] в типе карточки.  
[VisitExtensionAsync](M_Tessa_Cards_ICardTypeVisitor_VisitExtensionAsync.htm)|
Посещает объект [Tessa.Cards.CardTypeExtension] в типе карточки.  
[VisitNamedFormAsync](M_Tessa_Cards_ICardTypeVisitor_VisitNamedFormAsync.htm)|
Посещает объект [Tessa.Cards.CardTypeNamedForm] в типе карточки.  
[VisitSchemeItemAsync](M_Tessa_Cards_ICardTypeVisitor_VisitSchemeItemAsync.htm)|
Посещает объект [Tessa.Cards.CardTypeSchemeItem] в типе карточки.  
[VisitTabFormAsync](M_Tessa_Cards_ICardTypeVisitor_VisitTabFormAsync.htm)|
Посещает объект [Tessa.Cards.CardTypeTabForm] в типе карточки.  
[VisitTableFormAsync](M_Tessa_Cards_ICardTypeVisitor_VisitTableFormAsync.htm)|
Посещает объект [Tessa.Cards.CardTypeTableForm] в типе карточки.  
[VisitTypeFormAsync](M_Tessa_Cards_ICardTypeVisitor_VisitTypeFormAsync.htm)|
Посещает основную форму [Tessa.Cards.CardTypeTabForm] в типе карточки.  
[VisitValidatorAsync(CardTypeValidator, CardType,
CancellationToken)](M_Tessa_Cards_ICardTypeVisitor_VisitValidatorAsync.htm)|
Посещает объект [Tessa.Cards.CardTypeValidator] в типе карточки.  
[VisitValidatorAsync(CardTypeValidator, CardTypeCompletionOption, CardType,
CancellationToken)](M_Tessa_Cards_ICardTypeVisitor_VisitValidatorAsync_1.htm)|
Посещает объект [Tessa.Cards.CardTypeValidator] в типе карточки для варианта
завершения.  
## __См. также
#### Ссылки
[Tessa.Cards - пространство имён](N_Tessa_Cards.htm)
