# CardValidationExtensions - методы
##  __Методы
[GetLimitedCardResult](M_Tessa_Cards_Validation_CardValidationExtensions_GetLimitedCardResult.htm)|
Возвращает результат валидации для карточки с учётом ограничений, указываемых
в объекте
[ICardValidationLimitationManager](T_Tessa_Cards_Validation_ICardValidationLimitationManager.htm).  
---|---  
[GetValidationNotNullTableInfoList](M_Tessa_Cards_Validation_CardValidationExtensions_GetValidationNotNullTableInfoList.htm)|
Возвращает список объектов
[CardValidationNotNullTableInfo](T_Tessa_Cards_Validation_CardValidationNotNullTableInfo.htm)
для заданного хранилища storage или создаёт и возвращает новый список
объектов, если искомый список не был найден в хранилище. Метод не возвращает
значение null.  
[GetValidationTransactionActionInfoList](M_Tessa_Cards_Validation_CardValidationExtensions_GetValidationTransactionActionInfoList.htm)|
Возвращает список выполняемых в транзакции методов для заданного хранилища
storage или создаёт и возвращает новый список объектов, если искомый список не
был найден в хранилище. Метод не возвращает значение null. Используйте метод,
чтобы добавить действие, записывающее ошибку в результат валидации, когда о
наличии ошибки известно перед началом транзакции, но транзакция должна быть
запущена, чтобы выполнились другие валидаторы.  
[GetValidationUniqueInfoList](M_Tessa_Cards_Validation_CardValidationExtensions_GetValidationUniqueInfoList.htm)|
Возвращает список объектов
[CardValidationUniqueInfo](T_Tessa_Cards_Validation_CardValidationUniqueInfo.htm)
для заданного хранилища storage или создаёт и возвращает новый список
объектов, если искомый список не был найден в хранилище. Метод не возвращает
значение null.  
[RegisterDefaults](M_Tessa_Cards_Validation_CardValidationExtensions_RegisterDefaults.htm)|
Выполняет регистрацию валидаторов карточки, предоставляемых платформой, в
реестре валидаторов карточки.  
[TryGetValidationNotNullTableInfoList](M_Tessa_Cards_Validation_CardValidationExtensions_TryGetValidationNotNullTableInfoList.htm)|
Возвращает список объектов
[CardValidationNotNullTableInfo](T_Tessa_Cards_Validation_CardValidationNotNullTableInfo.htm)
для заданного хранилища storage или null, если искомый список не был найден в
хранилище.  
[TryGetValidationTransactionActionInfoList](M_Tessa_Cards_Validation_CardValidationExtensions_TryGetValidationTransactionActionInfoList.htm)|
Возвращает список выполняемых в транзакции методов для заданного хранилища
storage или null, если искомый список не был найден в хранилище.  
[TryGetValidationUniqueInfoList](M_Tessa_Cards_Validation_CardValidationExtensions_TryGetValidationUniqueInfoList.htm)|
Возвращает список объектов
[CardValidationUniqueInfo](T_Tessa_Cards_Validation_CardValidationUniqueInfo.htm)
для заданного хранилища storage или null, если искомый список не был найден в
хранилище.  
## __См. также
#### Ссылки
[CardValidationExtensions -
](T_Tessa_Cards_Validation_CardValidationExtensions.htm)
[Tessa.Cards.Validation - пространство имён](N_Tessa_Cards_Validation.htm)
