# ICardValidationResult - интерфейс
Результат валидации карточки, содержащий методы доступа к построенным
результату валидации для различных элементов проверяемой карточки.
## __Definition
 **Пространство имён:** [Tessa.Cards.Validation](N_Tessa_Cards_Validation.htm)  
 **Сборка:** Tessa (в Tessa.dll) Версия: 3.6.0.17
C# __Копировать
     public interface ICardValidationResult
VB __Копировать
     Public Interface ICardValidationResult
C++ __Копировать
     public interface class ICardValidationResult
F# __Копировать
     type ICardValidationResult = interface end
##  __Свойства
[Context](P_Tessa_Cards_Validation_ICardValidationResult_Context.htm)|
Контекст валидации, для которого был создан результат, или null, если
результат не связан с контекстом (например, он был пустой).  
---|---  
## __Методы
[GetCardResult](M_Tessa_Cards_Validation_ICardValidationResult_GetCardResult.htm)|
Возвращает результат валидации для всей карточки. Включает в себя результаты
валидации всех секций, строк и полей, входящих в проверенную карточку.  
---|---  
[GetEntryFieldResult](M_Tessa_Cards_Validation_ICardValidationResult_GetEntryFieldResult.htm)|
Возвращает результат валидации для заданного поля строковой секции.  
[GetSectionResult](M_Tessa_Cards_Validation_ICardValidationResult_GetSectionResult.htm)|
Возвращает результат валидации для строковой, коллекционной или древовидной
секции карточки. Включает в себя результаты валидации всех строк и полей,
входящих в проверенную секцию.  
[GetTableFieldResult](M_Tessa_Cards_Validation_ICardValidationResult_GetTableFieldResult.htm)|
Возвращает результат валидации для заданного поля строки коллекционной или
древовидной секции.  
[GetTableRowResult](M_Tessa_Cards_Validation_ICardValidationResult_GetTableRowResult.htm)|
Возвращает результат валидации для строки коллекционной или древовидной
секции. Включает в себя результаты валидации всех полей, входящих в
проверенную строку.  
## __Методы расширения
[GetLimitedCardResult](M_Tessa_Cards_Validation_CardValidationExtensions_GetLimitedCardResult.htm)|
Возвращает результат валидации для карточки с учётом ограничений, указываемых
в объекте
[ICardValidationLimitationManager](T_Tessa_Cards_Validation_ICardValidationLimitationManager.htm).  
(Определяется
[CardValidationExtensions](T_Tessa_Cards_Validation_CardValidationExtensions.htm))  
---|---  
##  __См. также
#### Ссылки
[Tessa.Cards.Validation - пространство имён](N_Tessa_Cards_Validation.htm)
