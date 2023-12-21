# ICardValidator - интерфейс
Валидатор карточки. Экземпляры валидаторов не должны иметь состояния, т.е.
полей, изменяемых со временем. Конструктор валидатора будет вызван в момент
регистрации экземпляра в реестре
[ICardValidatorRegistry](T_Tessa_Cards_Validation_ICardValidatorRegistry.htm).
## __Definition
 **Пространство имён:** [Tessa.Cards.Validation](N_Tessa_Cards_Validation.htm)  
 **Сборка:** Tessa (в Tessa.dll) Версия: 3.6.0.17
C# __Копировать
     public interface ICardValidator
VB __Копировать
     Public Interface ICardValidator
C++ __Копировать
     public interface class ICardValidator
F# __Копировать
     type ICardValidator = interface end
##  __Методы
[ValidateAsync](M_Tessa_Cards_Validation_ICardValidator_ValidateAsync.htm)|
Выполняет валидацию карточки, переданной в контексте context, с указанными в
validator настройками.  
---|---  
## __См. также
#### Ссылки
[Tessa.Cards.Validation - пространство имён](N_Tessa_Cards_Validation.htm)
