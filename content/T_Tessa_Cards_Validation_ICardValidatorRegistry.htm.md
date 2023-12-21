# ICardValidatorRegistry - интерфейс
Реестр валидаторов карточки.
## __Definition
 **Пространство имён:** [Tessa.Cards.Validation](N_Tessa_Cards_Validation.htm)  
 **Сборка:** Tessa (в Tessa.dll) Версия: 3.6.0.17
C# __Копировать
     public interface ICardValidatorRegistry
VB __Копировать
     Public Interface ICardValidatorRegistry
C++ __Копировать
     public interface class ICardValidatorRegistry
F# __Копировать
     type ICardValidatorRegistry = interface end
##  __Методы
[Get](M_Tessa_Cards_Validation_ICardValidatorRegistry_Get.htm)| Возвращает
экземпляр валидатора, тип которого был зарегистрирован в реестре по
метаинформации о типе этого валидатора.  
---|---  
[GetAll](M_Tessa_Cards_Validation_ICardValidatorRegistry_GetAll.htm)|
Возвращает коллекцию экземпляров валидаторов, типы которых были
зарегистрированы в реестре.  
[Register](M_Tessa_Cards_Validation_ICardValidatorRegistry_Register.htm)|
Выполняет регистрацию в реестре экземпляра валидатора заданного типа по
указанной метаинформации, который в дальнейшем может быть использован для
валидации карточки.  
## __Методы расширения
[RegisterDefaults](M_Tessa_Cards_Validation_CardValidationExtensions_RegisterDefaults.htm)|
Выполняет регистрацию валидаторов карточки, предоставляемых платформой, в
реестре валидаторов карточки.  
(Определяется
[CardValidationExtensions](T_Tessa_Cards_Validation_CardValidationExtensions.htm))  
---|---  
##  __См. также
#### Ссылки
[Tessa.Cards.Validation - пространство имён](N_Tessa_Cards_Validation.htm)
