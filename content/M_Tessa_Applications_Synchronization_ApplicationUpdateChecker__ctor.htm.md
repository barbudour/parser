# ApplicationUpdateChecker - конструктор
Initializes a new instance of the
[ApplicationUpdateChecker](T_Tessa_Applications_Synchronization_ApplicationUpdateChecker.htm)
class. Инициализирует новый экземпляр класса
[Object](https://learn.microsoft.com/dotnet/api/system.object).
## __Definition
 **Пространство имён:**
[Tessa.Applications.Synchronization](N_Tessa_Applications_Synchronization.htm)  
 **Сборка:** Tessa (в Tessa.dll) Версия: 3.6.0.17
C# __Копировать
     public ApplicationUpdateChecker(
    	[NotNullAttribute] ApplicationPackageBuilder packageBuilder,
    	[NotNullAttribute] IAvailableApplicationsQuery query
    )
VB __Копировать
     Public Sub New ( 
    	<NotNullAttribute> packageBuilder As ApplicationPackageBuilder,
    	<NotNullAttribute> query As IAvailableApplicationsQuery
    )
C++ __Копировать
     public:
    ApplicationUpdateChecker(
    	[NotNullAttribute] ApplicationPackageBuilder^ packageBuilder, 
    	[NotNullAttribute] IAvailableApplicationsQuery^ query
    )
F# __Копировать
     new : 
            [<NotNullAttribute>] packageBuilder : ApplicationPackageBuilder * 
            [<NotNullAttribute>] query : IAvailableApplicationsQuery -> ApplicationUpdateChecker
#### Параметры
packageBuilder
[ApplicationPackageBuilder](T_Tessa_Applications_Package_ApplicationPackageBuilder.htm)
     Построитель пакетов приложений 
query
[IAvailableApplicationsQuery](T_Tessa_Applications_Synchronization_IAvailableApplicationsQuery.htm)
     Запрос к карточке приложения 
## __См. также
#### Ссылки
[ApplicationUpdateChecker -
](T_Tessa_Applications_Synchronization_ApplicationUpdateChecker.htm)
[Tessa.Applications.Synchronization - пространство
имён](N_Tessa_Applications_Synchronization.htm)
