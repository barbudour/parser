# IValidationObject - интерфейс
Объект, поддерживающий валидацию свойств.
## __Definition
 **Пространство имён:**
[Tessa.Platform.Validation](N_Tessa_Platform_Validation.htm)  
 **Сборка:** Tessa (в Tessa.dll) Версия: 3.6.0.17
C# __Копировать
     public interface IValidationObject : IValidatable
VB __Копировать
     Public Interface IValidationObject
    	Inherits IValidatable
C++ __Копировать
     public interface class IValidationObject : IValidatable
F# __Копировать
     type IValidationObject = 
        interface
            interface IValidatable
        end
Implements
    [IValidatable](T_Tessa_Platform_Validation_IValidatable.htm)
##  __Методы
[IsValid](M_Tessa_Platform_Validation_IValidatable_IsValid.htm)| Выполняет
проверку объекта на валидность и возвращает признак того, что объект является
валидным.  
(Унаследован от [IValidatable](T_Tessa_Platform_Validation_IValidatable.htm))  
---|---  
[Validate](M_Tessa_Platform_Validation_IValidationObject_Validate.htm)|
Выполняет валидацию текущего объекта и всех его дочерних объектов.  
##  __Методы расширения
[Validate](M_Tessa_Platform_Validation_ValidationExtensions_Validate.htm)|
Выполняет валидацию объекта и всех его дочерних объектов.  
(Определяется
[ValidationExtensions](T_Tessa_Platform_Validation_ValidationExtensions.htm))  
---|---  
##  __См. также
#### Ссылки
[Tessa.Platform.Validation - пространство
имён](N_Tessa_Platform_Validation.htm)
