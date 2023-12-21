# Tessa.Views.Metadata.Criteria - пространство имён
Операторы критериев сравнения значений для API метаданных.
##  __Классы
[BetweenCriteriaOperator](T_Tessa_Views_Metadata_Criteria_BetweenCriteriaOperator.htm)|
Оператор - между(период)  
---|---  
[ContainsCriteriaOperator](T_Tessa_Views_Metadata_Criteria_ContainsCriteriaOperator.htm)|
Оператор содержит  
[CriteriaGenerationException](T_Tessa_Views_Metadata_Criteria_CriteriaGenerationException.htm)|
Исключение выдаваемое при ошибках генерации условий  
[CriteriaGeneratorHelper](T_Tessa_Views_Metadata_Criteria_CriteriaGeneratorHelper.htm)|
Вспомогательные методы для генераторов условий  
[CriteriaOperator](T_Tessa_Views_Metadata_Criteria_CriteriaOperator.htm)|
Базовое класс описания условного оператора. Условные операторы предназначены
для формирования запросов к представлениям
[ITessaViewRequest](T_Tessa_Views_ITessaViewRequest.htm),  
[CriteriaOperatorConst](T_Tessa_Views_Metadata_Criteria_CriteriaOperatorConst.htm)|
Класс содержащий названия операторов условий  
[CriteriaOperatorRegistration](T_Tessa_Views_Metadata_Criteria_CriteriaOperatorRegistration.htm)|
Осуществляет регистрацию в контейнере зависимостей требуемых для корректной
работы генераторов текста sql-выражений  
[CriteriaRegistry](T_Tessa_Views_Metadata_Criteria_CriteriaRegistry.htm)|
Реестр условий  
[EndsWithCriteriaOperator](T_Tessa_Views_Metadata_Criteria_EndsWithCriteriaOperator.htm)|
Оператор оканчивается на  
[EqualsCriteriaOperator](T_Tessa_Views_Metadata_Criteria_EqualsCriteriaOperator.htm)|
Оператор равенства. Создает выражение param_name = param_value, если
param_value = null будет создано выражение param_name is null.  
[GreatOrEqualsCriteriaOperator](T_Tessa_Views_Metadata_Criteria_GreatOrEqualsCriteriaOperator.htm)|
Оператор больше или равно  
[GreatThanCriteriaOperator](T_Tessa_Views_Metadata_Criteria_GreatThanCriteriaOperator.htm)|
Оператор больше чем  
[IsFalseCriteriaOperator](T_Tessa_Views_Metadata_Criteria_IsFalseCriteriaOperator.htm)|
Логический оператор ложь  
[IsNotNullCriteriaOperator](T_Tessa_Views_Metadata_Criteria_IsNotNullCriteriaOperator.htm)|
Оператор Is Not null  
[IsNullCriteriaOperator](T_Tessa_Views_Metadata_Criteria_IsNullCriteriaOperator.htm)|
Оператор Is Null  
[IsTrueCriteriaOperator](T_Tessa_Views_Metadata_Criteria_IsTrueCriteriaOperator.htm)|
Логический оператор истина  
[LessOrEqualsCriteriaOperator](T_Tessa_Views_Metadata_Criteria_LessOrEqualsCriteriaOperator.htm)|
Оператор меньше или равно  
[LessThanCriteriaOperator](T_Tessa_Views_Metadata_Criteria_LessThanCriteriaOperator.htm)|
Оператор меньше чем  
[LinkCriteriaOperator](T_Tessa_Views_Metadata_Criteria_LinkCriteriaOperator.htm)|
Условный оператор ссылка  
[NonEqualsCriteriaOperator](T_Tessa_Views_Metadata_Criteria_NonEqualsCriteriaOperator.htm)|
Оператор не равенства  
[OneValueCriteriaOperator](T_Tessa_Views_Metadata_Criteria_OneValueCriteriaOperator.htm)|
Базовый абстрактный класс для операторов сравнения поддерживающих одно
значение  
[PostgreSqlCriteriaOperatorRegistration](T_Tessa_Views_Metadata_Criteria_PostgreSqlCriteriaOperatorRegistration.htm)|
Осуществляет регистрацию в контейнере зависимостей требуемых для корректной
работы генераторов текста sql-выражений  
[SqlServerCriteriaOperatorRegistration](T_Tessa_Views_Metadata_Criteria_SqlServerCriteriaOperatorRegistration.htm)|
Осуществляет регистрацию в контейнере зависимостей требуемых для корректной
работы генераторов текста sql-выражений  
[StartsWithOperator](T_Tessa_Views_Metadata_Criteria_StartsWithOperator.htm)|
Оператор начинается с  
[TwoValueCriteriaOperator](T_Tessa_Views_Metadata_Criteria_TwoValueCriteriaOperator.htm)|
Базовый абстрактный класс для операторов сравнения поддерживающих два значения  
[ZeroValuesCriteriaOperator](T_Tessa_Views_Metadata_Criteria_ZeroValuesCriteriaOperator.htm)|
Базовый абстрактный класс для операторов сравнения не поддерживающих значения  
## __Интерфейсы
[ICriteriaGenerator](T_Tessa_Views_Metadata_Criteria_ICriteriaGenerator.htm)|
Описание интерфейса генератора условий  
---|---  
[IDbmsCriteriaGenerator](T_Tessa_Views_Metadata_Criteria_IDbmsCriteriaGenerator.htm)|  
## __Делегаты
[CriteriaGeneratorFactory](T_Tessa_Views_Metadata_Criteria_CriteriaGeneratorFactory.htm)|
Делегат фабрики получения генератора текста условия для подсистемы баз данных
dbms и условного оператора criteriaOperator  
---|---
