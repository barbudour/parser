# Tessa.Views - пространство имён
API представлений и рабочих мест.
##  __Классы
[AccessCacheSharedEventArgs](T_Tessa_Views_AccessCacheSharedEventArgs.htm)|
Аргументы события очистки кэша доступных пользователю представлений  
---|---  
[ColumnCountMismatchException](T_Tessa_Views_ColumnCountMismatchException.htm)|  
[DefaultValues](T_Tessa_Views_DefaultValues.htm)|  Значения по умолчанию в
виде {строковое представление, значение} для стандартных типов.  
[ExtensionSettingsSerializationHelper](T_Tessa_Views_ExtensionSettingsSerializationHelper.htm)|
Вспомогательные методы сохранения/загрузки настроек расширений в BSON  
[GetModelRequest](T_Tessa_Views_GetModelRequest.htm)|  Запрос для получения
списка элементов представлений/рабочих мест  
[ImportTessaViewRequest](T_Tessa_Views_ImportTessaViewRequest.htm)|
Реализация запроса к сервису
[ITessaViewService](T_Tessa_Views_ITessaViewService.htm) предназначенного для
импорта представлений  
[LocalizationHelper](T_Tessa_Views_LocalizationHelper.htm)|  Статические
методы для поддержки локализации представлений  
[MissedDataSourceMetadataAdapter](T_Tessa_Views_MissedDataSourceMetadataAdapter.htm)|
Адаптер отсутствующих метаданных  
[MsSqlQueryResultMetadataProvider](T_Tessa_Views_MsSqlQueryResultMetadataProvider.htm)|  
[NullDataSourceMetadataAdapter](T_Tessa_Views_NullDataSourceMetadataAdapter.htm)|
Пустой источник метаданных  
[NullSearchQueryMetadata](T_Tessa_Views_NullSearchQueryMetadata.htm)|
Фейковый класс для отображения пустых метаданных поискового запроса  
[NullViewMetadata](T_Tessa_Views_NullViewMetadata.htm)|  Метаданные
представления заменяющие значение null  
[PostgresQueryResultMetadataProvider](T_Tessa_Views_PostgresQueryResultMetadataProvider.htm)|  
[QueryResultMetadata](T_Tessa_Views_QueryResultMetadata.htm)|  Описание
метаинформации результатов выполнения запроса  
[QueryResultMetadataProvider](T_Tessa_Views_QueryResultMetadataProvider.htm)|
Предоставляет информацию о метаданных результа выполнения запроса к базе
данных  
[RequestParameterBuilder](T_Tessa_Views_RequestParameterBuilder.htm)|
Построитель параметра запроса к представлению  
[RoleLink](T_Tessa_Views_RoleLink.htm)|  Объект, хранящий привязку роли к
объекту.  
[SearchQueriesAccessor](T_Tessa_Views_SearchQueriesAccessor.htm)|
Осуществляет манипуляцию поисковыми запросами в базе данных  
[SearchQueryMetadataAdapter](T_Tessa_Views_SearchQueryMetadataAdapter.htm)|
Адаптер метаданных поискового запроса  
[SearchQueryService](T_Tessa_Views_SearchQueryService.htm)|  Серверная
реализация сервиса поисковых запросов  
[ServerViewServiceImplementer](T_Tessa_Views_ServerViewServiceImplementer.htm)|
Реализатор серверной части [IViewService](T_Tessa_Views_IViewService.htm)
сервиса представлений.  
[SortingColumn](T_Tessa_Views_SortingColumn.htm)|  Объект содержащего колонку
по которой осуществляется сортировка данных  
[SortingColumnCollection](T_Tessa_Views_SortingColumnCollection.htm)|  The
sorting column collection.  
[SortingColumnHelper](T_Tessa_Views_SortingColumnHelper.htm)|  Вспомогательные
методы для работы с установленными значениями сортировок столбцов
[ISortingColumn](T_Tessa_Views_ISortingColumn.htm)  
[StoreTessaViewRequest](T_Tessa_Views_StoreTessaViewRequest.htm)|  Запрос к
сервису [ITessaViewService](T_Tessa_Views_ITessaViewService.htm)
предназначенный для изменения списка представлений  
[SystemViewAliases](T_Tessa_Views_SystemViewAliases.htm)|  Алиасы некоторых
системных представлений.  
[TessaExchangeWorkplaceModel](T_Tessa_Views_TessaExchangeWorkplaceModel.htm)|
Модель используемая при обмене данными рабочего места.  
[TessaInvalidExchangeWorkplaceModel](T_Tessa_Views_TessaInvalidExchangeWorkplaceModel.htm)|
Класс описывающий исключение возникшее при работе с моделью обмена  
[TessaViewDecorator](T_Tessa_Views_TessaViewDecorator.htm)|  Декорирует классы
[представлений](T_Tessa_Views_ITessaView.htm) добавляет функционал
автоматического внедрения в список параметров
[запроса](T_Tessa_Views_ITessaViewRequest.htm) параметра [Идентификатор
текущего
пользователя](F_Tessa_Views_ViewSpecialParametersConst_CurrentUserId.htm)  
[TessaViewModel](T_Tessa_Views_TessaViewModel.htm)|  Данные представления.  
[TessaViewModelRepository](T_Tessa_Views_TessaViewModelRepository.htm)|
Репозиторий моделей представлений  
[TessaViewRequest](T_Tessa_Views_TessaViewRequest.htm)|  Запрос к
представлению.  
[TessaViewRequestHelper](T_Tessa_Views_TessaViewRequestHelper.htm)|  The tessa
view request helper.  
[TessaViewResult](T_Tessa_Views_TessaViewResult.htm)|  Результат выполнения
запроса  
[TessaViewResultHelper](T_Tessa_Views_TessaViewResultHelper.htm)|  The tessa
view result helper.  
[TessaViewService](T_Tessa_Views_TessaViewService.htm)|  The tessa view
service.  
[TessaViewServiceBinaryClient](T_Tessa_Views_TessaViewServiceBinaryClient.htm)|  
[TessaViewServiceClient](T_Tessa_Views_TessaViewServiceClient.htm)|  
[TessaViewServiceContext](T_Tessa_Views_TessaViewServiceContext.htm)|
Контекст для изменения текущего
[ITessaViewService](T_Tessa_Views_ITessaViewService.htm).  
[TessaViewServiceLegacy2X](T_Tessa_Views_TessaViewServiceLegacy2X.htm)|
Реализация веб-сервиса
[ITessaViewService](T_Tessa_Views_ITessaViewService.htm) для маршрута
[Legacy2X](T_Tessa_Platform_Runtime_ServiceRoute.htm). Сервис представлен в
ограниченном виде и пригоден только для обращения из Tessa Applications к
представлению "AvailableApplications".  
[TessaViewServiceProxy](T_Tessa_Views_TessaViewServiceProxy.htm)|  Прокси-
объект для [ITessaViewService](T_Tessa_Views_ITessaViewService.htm).  
[TessaViewServiceRouter](T_Tessa_Views_TessaViewServiceRouter.htm)|
Реализация веб-сервиса
[ITessaViewService](T_Tessa_Views_ITessaViewService.htm), которая выполняет
маршрутизацию посредством объекта
[IServiceRouter](T_Tessa_Platform_Runtime_IServiceRouter.htm).  
[TypeLiftingHelper](T_Tessa_Views_TypeLiftingHelper.htm)|  Вспомогаетльные
методы для преобразования типа  
[UnityExtraViewListProvider](T_Tessa_Views_UnityExtraViewListProvider.htm)|
Имплементация [провайдера](T_Tessa_Views_IExtraViewListProvider.htm)
представлений задаваемых программным путем. Используется для регистрации в
контейнере для проброса в классы зависящие от
[IExtraViewListProvider](T_Tessa_Views_IExtraViewListProvider.htm) в случае
отсутствия пользовательской регистрации
[провайдера](T_Tessa_Views_IExtraViewListProvider.htm). Всегда возвращает
пустой список [представлений](T_Tessa_Views_ITessaView.htm)  
[ViewAccessCache](T_Tessa_Views_ViewAccessCache.htm)|  Кэш доступов к
представлениям  
[ViewCardParameters](T_Tessa_Views_ViewCardParameters.htm)|  Предоставляет
параметры доступа к текущей карточке  
[ViewCurrentUserParameters](T_Tessa_Views_ViewCurrentUserParameters.htm)|
Представляет доступ к специальному параметру CurrentUserId  
[ViewDataAccessor](T_Tessa_Views_ViewDataAccessor.htm)|  DataAccesor
предоставляющий методы манипуляции моделями представлений сохраненым в базе
данных  
[ViewException](T_Tessa_Views_ViewException.htm)|  Исключение произошедшее при
выполнении представления.  
[ViewExecutionSettings](T_Tessa_Views_ViewExecutionSettings.htm)|  Настройки
исполнения представлений  
[ViewHelper](T_Tessa_Views_ViewHelper.htm)|  Предоставляет вспомогательные
методы для пространства имён Tessa.Views.  
[ViewInterceptorBase](T_Tessa_Views_ViewInterceptorBase.htm)|  Базовый класс
перехватчика представлений  
[ViewMetadataAdapter](T_Tessa_Views_ViewMetadataAdapter.htm)|  Адаптер
метаданных представления  
[ViewPagingParameters](T_Tessa_Views_ViewPagingParameters.htm)|  Представляет
параметры пейджинга  
[ViewQueryExecutor](T_Tessa_Views_ViewQueryExecutor.htm)|  Исполнитель
запросов представлений.  
[ViewRowHelper](T_Tessa_Views_ViewRowHelper.htm)|  Методы расширения для
[ITessaViewResult](T_Tessa_Views_ITessaViewResult.htm)  
[ViewsBinaryWebProxy](T_Tessa_Views_ViewsBinaryWebProxy.htm)|  Прокси для
обращения к веб-сервису
[ITessaViewService](T_Tessa_Views_ITessaViewService.htm).  
[ViewsCache](T_Tessa_Views_ViewsCache.htm)|  Потокобезопасный кэш
представлений  
[ViewService](T_Tessa_Views_ViewService.htm)|  Сервис представлений.
Предоставляет клиентам доступ к спискам
[представлений](T_Tessa_Views_ITessaView.htm) и
[метаданных](T_Tessa_Views_Metadata_IViewMetadata.htm) представлений.  
[ViewServiceHelper](T_Tessa_Views_ViewServiceHelper.htm)|  Методы расширения
для [IViewService](T_Tessa_Views_IViewService.htm)  
[ViewsExtensions](T_Tessa_Views_ViewsExtensions.htm)|  Методы-расширения для
пространства имён Tessa.Views.  
[ViewSpecialParameters](T_Tessa_Views_ViewSpecialParameters.htm)|  Класс
предназначенный для проставления специальных параметров используемых в
представлениях На текущий момент отрабатываются параметры CurrentUserID -
текущий пользователь PageOffset - смещение от начала списка PageLimit -
количество элементов на странице CardId - идентификатор текущей карточки
CardTypeId - идентификатор типа текущей карточки Locale - идентификатор локали  
[ViewSpecialParametersConst](T_Tessa_Views_ViewSpecialParametersConst.htm)|
Предопределенные параметры представлений.  
[ViewSpecialParametersMetadata](T_Tessa_Views_ViewSpecialParametersMetadata.htm)|
Метаданные специальных параметров  
[ViewsUnityClassRegistrator](T_Tessa_Views_ViewsUnityClassRegistrator.htm)|
Регистрация представлений в контейнере приложения  
[ViewsWebProxy](T_Tessa_Views_ViewsWebProxy.htm)|  Прокси для обращения к
контроллеру, обеспечивающему взаимодействие с представлениями.  
[WorkplaceDataAccessor](T_Tessa_Views_WorkplaceDataAccessor.htm)|  Акссесор
для получения моделей рабочих мест из БД  
## __Интерфейсы
[ICurrentUserViewService](T_Tessa_Views_ICurrentUserViewService.htm)|
Интерфейс сервиса [IViewService](T_Tessa_Views_IViewService.htm) с
ограничением на предоставление представлений только текущему пользователю  
---|---  
[IDataSourceMetadata](T_Tessa_Views_IDataSourceMetadata.htm)|  Описание
интерфейса предоставляющего доступ к метаданным источника данных
(представления)  
[IDbmsQueryResultMetadataProvider](T_Tessa_Views_IDbmsQueryResultMetadataProvider.htm)|
Описание интерфейса для объектов предоставляющих метаинформацию из результатов
выполнения запроса к представлению  
[IExtraViewListProvider](T_Tessa_Views_IExtraViewListProvider.htm)|  Интерфейс
возвращающий список программных представлений  
[IExtraViewProvider](T_Tessa_Views_IExtraViewProvider.htm)|
Интерфейс, предоставляющий доступ к объекту программного представления с
собственной метаинформацией и логикой выполнения.
Классы, реализующие интерфейс, должны быть зарегистрированы в Unity по разным
именам: UnityContainer.RegisterType<IExtraViewProvider,
MyComputedViewProvider>(nameof(MyComputedViewProvider), new
ContainerControlledLifetimeManager());  
[IGetModelRequest](T_Tessa_Views_IGetModelRequest.htm)|  Интерфейс запроса к
сервису представлений для получения списка моделей представлений.  
[IGetModelResponse<T>](T_Tessa_Views_IGetModelResponse_1.htm)|  Результат
выполнения запроса к сервисам  
[IItemShowMode](T_Tessa_Views_IItemShowMode.htm)|  Описание интерфейса режима
отображения элемента рабочего места  
[IObjectCloneable<T>](T_Tessa_Views_IObjectCloneable_1.htm)|  Интерфейс
клонирования объекта  
[IQueryExecutorResultWriter](T_Tessa_Views_IQueryExecutorResultWriter.htm)|
Интерфейс объектов осуществляющих создание данных ITessaViewResult  
[IReadOnlyMarker](T_Tessa_Views_IReadOnlyMarker.htm)|  Интерфейс объекта с
поддержкой состояния только для чтения  
[IRepository<TGetRequest, TChangeRequest,
TResponse>](T_Tessa_Views_IRepository_3.htm)|  Интерфейс хранилища объектов  
[ISecurityDescriptor](T_Tessa_Views_ISecurityDescriptor.htm)|  Описание
интерфейса объекта поддерживающего ролевой доступ  
[ISortingColumn](T_Tessa_Views_ISortingColumn.htm)|  Интерфейс контракт с
колонкой сортировки.  
[IStoreModelRequest<T>](T_Tessa_Views_IStoreModelRequest_1.htm)|  Интерфейс
запроса на изменение списка моделей  
[IStoreTessaViewRequest](T_Tessa_Views_IStoreTessaViewRequest.htm)|  Интерфейс
запроса к сервису представлений
[ITessaViewService](T_Tessa_Views_ITessaViewService.htm)  
[IStreamedViewService](T_Tessa_Views_IStreamedViewService.htm)|  Описание
интерфейса предоставляющего доступ к результатам выполнения запроса в виде
потока.  
[ITessaView](T_Tessa_Views_ITessaView.htm)|  Базовый интерфейс представления.
Предназначен для имплементации представлений. Представления - произвольные
источники данных позволяющие выполнять к ним
[запросы](T_Tessa_Views_ITessaViewRequest.htm) на получение
[данных](T_Tessa_Views_ITessaViewResult.htm). Представление содержит
[метаданные](T_Tessa_Views_Metadata_IViewMetadata.htm) описывающие возможные
параметры запроса к представлению и детали визуализации результата.  
[ITessaViewAccess](T_Tessa_Views_ITessaViewAccess.htm)|  Интерфейс
предоставляющий информацию о доступе к представлению.  
[ITessaViewOverlay](T_Tessa_Views_ITessaViewOverlay.htm)|  Описание интерфейса
предназначенного для расширенной реализации клиентских программных
представлениях Классы реализующие данный интерфейс получают возможность а)
Получить ссылку на серверное представление с алиасом
[ViewAlias](P_Tessa_Views_ITessaViewOverlay_ViewAlias.htm) б) Осуществить
проверку необходимости регистрации клиентского представления  
[ITessaViewRequest](T_Tessa_Views_ITessaViewRequest.htm)|  Описание интерфейса
запроса к представлению [ITessaView](T_Tessa_Views_ITessaView.htm). Запрос
содержит информацию необходимую для осуществления вызова представления
указанного в [View](P_Tessa_Views_ITessaViewRequest_View.htm) с параметрами
[Values](P_Tessa_Views_ITessaViewRequest_Values.htm). Для получения из
представления результатов подмножества необходимо задать имя подмножества в
[SubsetName](P_Tessa_Views_ITessaViewRequest_SubsetName.htm). Значения
заданные в [SortingColumn](T_Tessa_Views_SortingColumn.htm) влияют на
сортировку результатов выполнения представления. Результат выполнения запроса
к представлению возвращается в виде объекта реализующего интерфейс
[ITessaViewResult](T_Tessa_Views_ITessaViewResult.htm)  
[ITessaViewResult](T_Tessa_Views_ITessaViewResult.htm)|  Интерфейс результатов
запросов к представлению  
[ITessaViewService](T_Tessa_Views_ITessaViewService.htm)|  Интерфейс сервиса
представлений  
[ITessaViewServiceContext](T_Tessa_Views_ITessaViewServiceContext.htm)|
Контекст для изменения текущего
[ITessaViewService](T_Tessa_Views_ITessaViewService.htm).  
[ITessaViewServiceLegacy](T_Tessa_Views_ITessaViewServiceLegacy.htm)|  
[ITessaViewsInterceptor](T_Tessa_Views_ITessaViewsInterceptor.htm)|  Интерфейс
перехвата выполнения запроса к представлению  
[IViewCardParameters](T_Tessa_Views_IViewCardParameters.htm)|  Интерфейс
представляющий доступ к формированию специальных параметров типа и
идентификатора карточки  
[IViewConnectionInfo](T_Tessa_Views_IViewConnectionInfo.htm)|  Объект,
содержащий информацию о соединении, которое используется при выполнении
представления.  
[IViewCurrentUserParameters](T_Tessa_Views_IViewCurrentUserParameters.htm)|
Интерфейс представляющий доступ к параметрам CurrentUserId и текущей локали  
[IViewInterceptor](T_Tessa_Views_IViewInterceptor.htm)|  Интерфейс
перехватчика представлений  
[IViewPagingParameters](T_Tessa_Views_IViewPagingParameters.htm)|  Интерфейс
представляющий доступ к параметрам пейджинга  
[IViewQueryExecutor](T_Tessa_Views_IViewQueryExecutor.htm)|  Интерфейс
исполнителя запросов к базе данных для получения результатов представлений  
[IViewService](T_Tessa_Views_IViewService.htm)|  Описание интерфейса сервиса
представлений. Сервис предоставляет доступ к представлениям доступным в
системе.  
[IViewServiceImplementer](T_Tessa_Views_IViewServiceImplementer.htm)|
Описание интерфейса для объектов являющихся конечными реализациями которым
делегирует выполнение методов сервис представлений
[ViewService](T_Tessa_Views_ViewService.htm)  
[IViewServiceInitializer](T_Tessa_Views_IViewServiceInitializer.htm)|  
[IViewSpecialParameters](T_Tessa_Views_IViewSpecialParameters.htm)|  Интерфейс
для предоставления методов внедрения специальных параметров Представлений в
список параметров  
[IViewTextGenerator](T_Tessa_Views_IViewTextGenerator.htm)|  Описание
интерфейса генератора текста sql запроса представления
[ITessaView](T_Tessa_Views_ITessaView.htm) по запросу к представлению
[ITessaViewRequest](T_Tessa_Views_ITessaViewRequest.htm).  
[IWorkplaceServiceInitializer](T_Tessa_Views_IWorkplaceServiceInitializer.htm)|
Описание интерфейса инициализации сервиса рабочих мест  
## __Делегаты
[TessaViewFactory](T_Tessa_Views_TessaViewFactory.htm)|  Делегат фабрики
создания представления  
---|---  
[ViewQueryGenerator](T_Tessa_Views_ViewQueryGenerator.htm)|  Делагат
осуществляющий построение текста выражения для представления в соответствии с
метаданными viewMetadata и запросом к представлению request, результат
выполнения запроса будет помещен в буфер вывода builder  
##  __Перечисления
[MetadataDataSourceTypes](T_Tessa_Views_MetadataDataSourceTypes.htm)|  Имена
типов источников данных  
---|---  
[Paging](T_Tessa_Views_Paging.htm)|  Поддержка постраничного вывода  
[PositionContext](T_Tessa_Views_PositionContext.htm)|  Тип текущего
местоположения в тексте  
[ShowMode](T_Tessa_Views_ShowMode.htm)|  Режим отображения элемента
