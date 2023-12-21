# Tessa.Platform.Placeholders - пространство имён
API для поиска и замены плейсхолдеров.
##  __Классы
[AliasPlaceholderContext](T_Tessa_Platform_Placeholders_AliasPlaceholderContext.htm)|
Часть контекста операции, содержащая информацию по алиасам плейсхолдеров.  
---|---  
[AliasPlaceholderParser](T_Tessa_Platform_Placeholders_AliasPlaceholderParser.htm)|
Объект, выполняющий распознание найденного в документе плейсхолдера с алиасом
{*Alias}.  
[AliasPlaceholderReplacer](T_Tessa_Platform_Placeholders_AliasPlaceholderReplacer.htm)|
Базовый класс для объекта, выполняющего замену плейсхолдера определённого
типа, работающего в режиме "замена по алиасу".  
[AliasPlaceholderReplacerNames](T_Tessa_Platform_Placeholders_AliasPlaceholderReplacerNames.htm)|
Название объекта, зарегистрированного по интерфейсу
[IAliasPlaceholderReplacer](T_Tessa_Platform_Placeholders_IAliasPlaceholderReplacer.htm).  
[AliasPlaceholderType](T_Tessa_Platform_Placeholders_AliasPlaceholderType.htm)|
Тип плейсхолдера, определяющего замену для плейсхолдера по алиасу.  
[AlignPlaceholderFormatter](T_Tessa_Platform_Placeholders_AlignPlaceholderFormatter.htm)|
Объект, выполняющий выравнивание строки текста с пробельными отступами и
выравниванием по левому краю, правому краю или по центру. Значения, отличные
от текстовых, считает пустой строкой.
Пример: {f:DocumentCommonInfo.Subject:#align(left=16)}
Допустимы значения выравнивания: left, right, center.  
[BarcodePlaceholderFormatter](T_Tessa_Platform_Placeholders_BarcodePlaceholderFormatter.htm)|
Объект, выполняющий форматирование значения поля из строки в штрих-код
определённого формата, представленный в виде изображения в формате PNG.
Пример: {fv:Content:#barcode}
Пример: {fv:Content:#barcode(w=250;h=80;t=ISBN)}  
[CardLinkPlaceholderFormatter](T_Tessa_Platform_Placeholders_CardLinkPlaceholderFormatter.htm)|
Заменяет уникальный идентификатор на ссылку на карточку с этим идентификатором
для web-клиента.  
[ContainerPlaceholderParser](T_Tessa_Platform_Placeholders_ContainerPlaceholderParser.htm)|  
[DefaultAliasPlaceholderReplacer](T_Tessa_Platform_Placeholders_DefaultAliasPlaceholderReplacer.htm)|
Объект, выполняющий замену плейсхолдера типа {*Alias}, работающего в режиме
"замена по алиасу".  
[DefaultFieldPlaceholderReplacer](T_Tessa_Platform_Placeholders_DefaultFieldPlaceholderReplacer.htm)|
Объект, выполняющий замену плейсхолдера типа {f:...}, работающего в режиме
"поле".  
[DefaultPlaceholderFormatter](T_Tessa_Platform_Placeholders_DefaultPlaceholderFormatter.htm)|
Объект, выполняющий форматирование значений для плейсхолдеров с выполнением
нестандартных форматтеров.  
[DefaultTablePlaceholderReplacer](T_Tessa_Platform_Placeholders_DefaultTablePlaceholderReplacer.htm)|
Объект, выполняющий замену плейсхолдера типа {t:...}, работающего в режиме
"таблица".  
[DefinitionPlaceholderParser](T_Tessa_Platform_Placeholders_DefinitionPlaceholderParser.htm)|
Объект, выполняющий распознание найденного в документе плейсхолдера описания
{#alias ...}.  
[DefinitionPlaceholderType](T_Tessa_Platform_Placeholders_DefinitionPlaceholderType.htm)|
Базовый класс для типа плейсхолдера.  
[EditablePlaceholderTable](T_Tessa_Platform_Placeholders_EditablePlaceholderTable.htm)|
Редактируемая таблица с данными плейсхолдера таблиц
[ITablePlaceholderType](T_Tessa_Platform_Placeholders_ITablePlaceholderType.htm).  
[FieldPlaceholderReplacer](T_Tessa_Platform_Placeholders_FieldPlaceholderReplacer.htm)|
Базовый класс для объекта, выполняющего замену плейсхолдера определённого
типа, работающего в режиме "поле".  
[FieldPlaceholderReplacer.CachedReplacement](T_Tessa_Platform_Placeholders_FieldPlaceholderReplacer_CachedReplacement.htm)|
Элемент кэша, по которому может быть выполнена замена плейсхолдера без
обращения к внешним источникам (к базе данных, представлению и др.).  
[FieldPlaceholderReplacerNames](T_Tessa_Platform_Placeholders_FieldPlaceholderReplacerNames.htm)|
Название объекта, зарегистрированного по интерфейсу
[IFieldPlaceholderReplacer](T_Tessa_Platform_Placeholders_IFieldPlaceholderReplacer.htm).  
[FieldPlaceholderType](T_Tessa_Platform_Placeholders_FieldPlaceholderType.htm)|
Тип плейсхолдера с режимом работы "поле"
[Field](T_Tessa_Platform_Placeholders_PlaceholderMode.htm).  
[FilePlaceholderFormatter](T_Tessa_Platform_Placeholders_FilePlaceholderFormatter.htm)|
Заменяет уникальный идентификатор на содержимое файла или версии файла с этим
идентификатором.
Пример: {t:Files.VersionRowID:#file(version);image}  
[FormatPlaceholderFormatter](T_Tessa_Platform_Placeholders_FormatPlaceholderFormatter.htm)|
Форматтер, выполняющий стандартное форматирование значения, полученного как:
#format(f=dd.MM.yyyy) или #format(localize)  
[HtmlPlaceholderDocument](T_Tessa_Platform_Placeholders_HtmlPlaceholderDocument.htm)|
Объект, определяющий способы хранения и изменения текста в формате HTML с
заменяемыми плейсхолдерами для строки
[String](https://learn.microsoft.com/dotnet/api/system.string).  
[ImagePlaceholderFormatter](T_Tessa_Platform_Placeholders_ImagePlaceholderFormatter.htm)|
Объект, выполняющий форматирование значения поля из массива байт или из строки
Base64 в изображение. Если тип данных значения несовместим или не
конвертируется из строки Base64, то будет выполнено стандартное форматирование
значения в строку.
Пример: {fv:Content:#image}
Пример: {fv:Content:#image(w=640;h=480;png;reformat)}  
[InfoFieldPlaceholderReplacer](T_Tessa_Platform_Placeholders_InfoFieldPlaceholderReplacer.htm)|
Объект, выполняющий замену плейсхолдера типа {info:...}, работающего в режиме
"поле".  
[LocalizePlaceholderParser](T_Tessa_Platform_Placeholders_LocalizePlaceholderParser.htm)|
Объект, выполняющий распознание найденного в документе плейсхолдера со строкой
локализации {$StringAlias}.  
[NoEncodePlaceholderFormatter](T_Tessa_Platform_Placeholders_NoEncodePlaceholderFormatter.htm)|
Форматер, который определяет необходимость запрета вызова методов encode при
обработке плейсхолдера (в частности, для Html)  
[NumberPlaceholderParser](T_Tessa_Platform_Placeholders_NumberPlaceholderParser.htm)|
Объект, выполняющий распознание найденного в документе плейсхолдера с номером
{0000n}. Если в контексте присутствует числовой номер по ключу
[NumberKey](F_Tessa_Platform_Placeholders_PlaceholderHelper_NumberKey.htm), то
плейсхолдер сразу заменяется на отформатированный вариант этого номера. В
противном случае плейсхолдер работает в режиме таблицы аналогично
плейсхолдеру: {tn:00000}.  
[NumberTablePlaceholderReplacer](T_Tessa_Platform_Placeholders_NumberTablePlaceholderReplacer.htm)|
Объект, выполняющий замену плейсхолдера типа {tn:...}, работающего в режиме
"таблица". Плейсхолдер возвращает отформатированный номер строки
[Number](P_Tessa_Platform_Placeholders_IPlaceholderRow_Number.htm).  
[Placeholder](T_Tessa_Platform_Placeholders_Placeholder.htm)|  Информация по
распознанному плейсхолдеру.  
[PlaceholderAggregateParser](T_Tessa_Platform_Placeholders_PlaceholderAggregateParser.htm)|
Объект, выполняющий распознание найденного в документе плейсхолдера на
основании последовательного вызова нескольких добавленных объектов
[IPlaceholderParser](T_Tessa_Platform_Placeholders_IPlaceholderParser.htm).  
[PlaceholderCollection](T_Tessa_Platform_Placeholders_PlaceholderCollection.htm)|
Коллекция объектов
[IPlaceholder](T_Tessa_Platform_Placeholders_IPlaceholder.htm).  
[PlaceholderContainer](T_Tessa_Platform_Placeholders_PlaceholderContainer.htm)|
Контейнер, содержащий регистрации типов плейсхолдеров.  
[PlaceholderContext](T_Tessa_Platform_Placeholders_PlaceholderContext.htm)|
Базовый класс для контекста операции, связанной с плейсхолдерами.  
[PlaceholderCustomFormat](T_Tessa_Platform_Placeholders_PlaceholderCustomFormat.htm)|
Настройки нестандартного форматирования.  
[PlaceholderCustomFormatParser](T_Tessa_Platform_Placeholders_PlaceholderCustomFormatParser.htm)|
Объект, выполняющий разбор настроек нестандартного форматирования по строке.  
[PlaceholderDocument](T_Tessa_Platform_Placeholders_PlaceholderDocument.htm)|
Базовый объект, определяющий способы хранения и изменения текста с заменяемыми
плейсхолдерами.  
[PlaceholderExecutableQuery](T_Tessa_Platform_Placeholders_PlaceholderExecutableQuery.htm)|
Запрос плейсхолдера к базе данных, подготовленный для выполнения.  
[PlaceholderExecutor](T_Tessa_Platform_Placeholders_PlaceholderExecutor.htm)|
Базовый класс для объектов, выполняющих выполнение запросов и получение
значений из базы данных, представлений или других внешних источников.  
[PlaceholderExtensions](T_Tessa_Platform_Placeholders_PlaceholderExtensions.htm)|
Методы-расширения для пространства имён Tessa.Platform.Placeholders.  
[PlaceholderFindingContext](T_Tessa_Platform_Placeholders_PlaceholderFindingContext.htm)|
Контекст операции, связанной с поиском плейсхолдеров.  
[PlaceholderFormatRequest](T_Tessa_Platform_Placeholders_PlaceholderFormatRequest.htm)|
Запрос на выполнение форматирования для значения плейсхолдера.  
[PlaceholderFormatResult](T_Tessa_Platform_Placeholders_PlaceholderFormatResult.htm)|
Результат выполненного форматирования для поля или набора полей.  
[PlaceholderFormatSettings](T_Tessa_Platform_Placeholders_PlaceholderFormatSettings.htm)|
Настройки форматирования для вывода значений.  
[PlaceholderFormatterBase](T_Tessa_Platform_Placeholders_PlaceholderFormatterBase.htm)|
Базовый объект, выполняющий форматирование значений для плейсхолдеров.
Определяет стандартный способ агрегации значений, но не форматирования.  
[PlaceholderFormatterContainer](T_Tessa_Platform_Placeholders_PlaceholderFormatterContainer.htm)|
Контейнер, содержащий регистрации, выполняющих нестандартное форматирование
значений для плейсхолдеров.  
[PlaceholderGroup](T_Tessa_Platform_Placeholders_PlaceholderGroup.htm)|
Коллекция объектов, для которой доступны уведомление об изменениях и
клонирование.  
[PlaceholderGroupCollection](T_Tessa_Platform_Placeholders_PlaceholderGroupCollection.htm)|
Коллекция объектов, для которой доступны уведомление об изменениях и
клонирование.  
[PlaceholderGrouping](T_Tessa_Platform_Placeholders_PlaceholderGrouping.htm)|
Объект с информацией по группировки данных в таблице, строки которой
наполняются через плейсхолдер в режиме "таблица".  
[PlaceholderGroupingCollection](T_Tessa_Platform_Placeholders_PlaceholderGroupingCollection.htm)|
Коллекция объектов
[IPlaceholderGrouping](T_Tessa_Platform_Placeholders_IPlaceholderGrouping.htm),
используемых для группировки строк в таблицах в запросах плейсхолдеров к базе
данных.  
[PlaceholderHelper](T_Tessa_Platform_Placeholders_PlaceholderHelper.htm)|
Вспомогательные средства для API плейсхолдеров.  
[PlaceholderImageParameters](T_Tessa_Platform_Placeholders_PlaceholderImageParameters.htm)|
Параметры, связанные с выводом плейсхолдеров-изображений.  
[PlaceholderImageTypes](T_Tessa_Platform_Placeholders_PlaceholderImageTypes.htm)|
Типы изображений, допустимые для свойства
[ImageType](P_Tessa_Platform_Placeholders_IPlaceholderImageParameters_ImageType.htm).
Также могут быть использованы другие типы MIME-содержимого.  
[PlaceholderInfoQueryExecutor](T_Tessa_Platform_Placeholders_PlaceholderInfoQueryExecutor.htm)|
Объект, выполняющий построение и выполнение запроса по объекту
[IPlaceholderQuery](T_Tessa_Platform_Placeholders_IPlaceholderQuery.htm).  
[PlaceholderInfoQueryParser](T_Tessa_Platform_Placeholders_PlaceholderInfoQueryParser.htm)|
Объект, выполняющий разбор выражения для запроса к базе данных для Info
Dictionary<string, object>.  
[PlaceholderJoin](T_Tessa_Platform_Placeholders_PlaceholderJoin.htm)|  Объект
с информацией по объединению таблиц, который строится по плейсхолдеру. Обычно
соответствует выражению: -(Join)->Section.Field. Свойство
[Join](P_Tessa_Platform_Placeholders_PlaceholderJoin_Join.htm) равно null для
первого элемента в списке и не равно null для всех прочих.  
[PlaceholderJoinCollection](T_Tessa_Platform_Placeholders_PlaceholderJoinCollection.htm)|
Коллекция объектов
[IPlaceholderJoin](T_Tessa_Platform_Placeholders_IPlaceholderJoin.htm),
используемых для объединения таблиц в запросах плейсхолдеров к базе данных.  
[PlaceholderManager](T_Tessa_Platform_Placeholders_PlaceholderManager.htm)|
Объект, управляющий операциями с плейсхолдерами.  
[PlaceholderParser<TContext>](T_Tessa_Platform_Placeholders_PlaceholderParser_1.htm)|
Базовый класс для объекта, выполняющего разбор выражения плейсхолдера для
запроса данных.  
[PlaceholderParsingContext](T_Tessa_Platform_Placeholders_PlaceholderParsingContext.htm)|
Базовый класс для контекста операции, выполняющей разбор выражения
плейсхолдера.  
[PlaceholderParsingEventArgs](T_Tessa_Platform_Placeholders_PlaceholderParsingEventArgs.htm)|
Аргументы событий, связанных с операцией по разбору плейсхолдера.  
[PlaceholderPatternBuilder](T_Tessa_Platform_Placeholders_PlaceholderPatternBuilder.htm)|
Объект, выполняющий построение шаблона регулярного выражения, выполняющего
разбор текста в параметрах плейсхолдера на составные части.  
[PlaceholderQuery](T_Tessa_Platform_Placeholders_PlaceholderQuery.htm)|
Запрос к базе данных, который строится по плейсхолдеру.  
[PlaceholderQueryBuilder](T_Tessa_Platform_Placeholders_PlaceholderQueryBuilder.htm)|
Объект, выполняющий формирование текста запроса по объекту
[IPlaceholderQuery](T_Tessa_Platform_Placeholders_IPlaceholderQuery.htm).  
[PlaceholderQueryBuilder.BuildContext](T_Tessa_Platform_Placeholders_PlaceholderQueryBuilder_BuildContext.htm)|
Контекст метода [Build(IPlaceholderReplacementContext, IQueryBuilderFactory,
IPlaceholder, IPlaceholderQuery, PlaceholderQueryBuilderFlags,
IEditablePlaceholderTable)](M_Tessa_Platform_Placeholders_PlaceholderQueryBuilder_Build.htm),
выполняющего построение запроса по объекту
[IPlaceholderQuery](T_Tessa_Platform_Placeholders_IPlaceholderQuery.htm).  
[PlaceholderQueryExecutor](T_Tessa_Platform_Placeholders_PlaceholderQueryExecutor.htm)|
Объект, выполняющий построение и выполнение запроса по объекту
[IPlaceholderQuery](T_Tessa_Platform_Placeholders_IPlaceholderQuery.htm).
Запрос может не выполняться на базе данных, например, если требуемые данные
содержатся в карточке.  
[PlaceholderQueryObject](T_Tessa_Platform_Placeholders_PlaceholderQueryObject.htm)|
Базовый класс для объекта запроса к базе данных, который строится по
плейсхолдеру.  
[PlaceholderQueryParser](T_Tessa_Platform_Placeholders_PlaceholderQueryParser.htm)|
Объект, выполняющий разбор выражения для запроса к базе данных.  
[PlaceholderQueryParsingContext](T_Tessa_Platform_Placeholders_PlaceholderQueryParsingContext.htm)|
Контекст операции, выполняющей разбор выражения плейсхолдера для объекта
[IPlaceholderQueryParser](T_Tessa_Platform_Placeholders_IPlaceholderQueryParser.htm).  
[PlaceholderRegexes](T_Tessa_Platform_Placeholders_PlaceholderRegexes.htm)|
Регулярные выражения, используемые при анализе некоторых видов плейсхолдеров,
таких как {f:...} или {t:...}.  
[PlaceholderReplacement](T_Tessa_Platform_Placeholders_PlaceholderReplacement.htm)|
Объект с информацией по способу замены плейсхолдера.  
[PlaceholderReplacementContext](T_Tessa_Platform_Placeholders_PlaceholderReplacementContext.htm)|
Контекст операции, связанной с заменой плейсхолдеров.  
[PlaceholderReplacementEventArgs](T_Tessa_Platform_Placeholders_PlaceholderReplacementEventArgs.htm)|
Аргументы событий, связанных с операцией по замене плейсхолдера.  
[PlaceholderRow](T_Tessa_Platform_Placeholders_PlaceholderRow.htm)|  Строка с
данными для плейсхолдера таблиц
[ITablePlaceholderType](T_Tessa_Platform_Placeholders_ITablePlaceholderType.htm).  
[PlaceholderRowKey](T_Tessa_Platform_Placeholders_PlaceholderRowKey.htm)|
Ключ, по которому осуществляется группировка строк
[IPlaceholderRow](T_Tessa_Platform_Placeholders_IPlaceholderRow.htm) в таблице
[IPlaceholderTable](T_Tessa_Platform_Placeholders_IPlaceholderTable.htm).  
[PlaceholderSorting](T_Tessa_Platform_Placeholders_PlaceholderSorting.htm)|
Объект с информацией по сортировке результатов запроса, который строится по
плейсхолдеру.  
[PlaceholderSortingCollection](T_Tessa_Platform_Placeholders_PlaceholderSortingCollection.htm)|
Коллекция объектов
[IPlaceholderSorting](T_Tessa_Platform_Placeholders_IPlaceholderSorting.htm),
используемых для сортировки результатов в запросах плейсхолдеров к базе
данных.  
[PlaceholderTable](T_Tessa_Platform_Placeholders_PlaceholderTable.htm)|
Таблица с данными плейсхолдера таблиц
[ITablePlaceholderType](T_Tessa_Platform_Placeholders_ITablePlaceholderType.htm).  
[PlaceholderTaskQueryExecutor](T_Tessa_Platform_Placeholders_PlaceholderTaskQueryExecutor.htm)|
Объект, выполняющий построение и выполнение запроса по объекту
[IPlaceholderQuery](T_Tessa_Platform_Placeholders_IPlaceholderQuery.htm).
Запрос может не выполняться на базе данных, например, если требуемые данные
содержатся в карточке.  
[PlaceholderTaskQueryParser](T_Tessa_Platform_Placeholders_PlaceholderTaskQueryParser.htm)|
Объект, выполняющий разбор выражения для запроса к базе данных для задания
[CardTask](T_Tessa_Cards_CardTask.htm).  
[PlaceholderText](T_Tessa_Platform_Placeholders_PlaceholderText.htm)|
Информация по плейсхолдеру, найденная в документе.  
[PlaceholderType](T_Tessa_Platform_Placeholders_PlaceholderType.htm)|  Базовый
класс для типа плейсхолдера.  
[PlaceholderValue](T_Tessa_Platform_Placeholders_PlaceholderValue.htm)|
Значение, на которое заменяется плейсхолдер. Содержит текст и опциональный
список полей, по которым был построен текст, с указанием типов каждого поля.
Любое строковое значение
[String](https://learn.microsoft.com/dotnet/api/system.string) может быть
неявно преобразовано к типу
[PlaceholderValue](T_Tessa_Platform_Placeholders_PlaceholderValue.htm).  
[PlaceholderValueType](T_Tessa_Platform_Placeholders_PlaceholderValueType.htm)|
Тип значения плейсхолдера. Нестандартное форматирование может вернуть тип,
отличный от строки.  
[PlaceholderValueTypeRegistry](T_Tessa_Platform_Placeholders_PlaceholderValueTypeRegistry.htm)|
Реестр типов значений плейсхолдеров
[PlaceholderValueType](T_Tessa_Platform_Placeholders_PlaceholderValueType.htm).
Класс является синглтоном.  
[PlaceholderValueTypes](T_Tessa_Platform_Placeholders_PlaceholderValueTypes.htm)|
Стандартные типы значений плейсхолдеров.  
[PlaceholderViewExecutor](T_Tessa_Platform_Placeholders_PlaceholderViewExecutor.htm)|
Объект, выполняющий построение и выполнение представления по запросу
[IPlaceholderViewRequest](T_Tessa_Platform_Placeholders_IPlaceholderViewRequest.htm).  
[PlaceholderViewParser](T_Tessa_Platform_Placeholders_PlaceholderViewParser.htm)|
Объект, выполняющий разбор выражения для запроса к представлению.  
[PlaceholderViewParsingContext](T_Tessa_Platform_Placeholders_PlaceholderViewParsingContext.htm)|
Контекст операции, выполняющей разбор выражения плейсхолдера для объекта
[IPlaceholderViewParser](T_Tessa_Platform_Placeholders_IPlaceholderViewParser.htm).  
[PlaceholderViewQueryBuilder](T_Tessa_Platform_Placeholders_PlaceholderViewQueryBuilder.htm)|
Объект, выполняющий формирование текста запроса по объекту
[IPlaceholderQuery](T_Tessa_Platform_Placeholders_IPlaceholderQuery.htm),
построенному по запросу к представлению
[IPlaceholderViewRequest](T_Tessa_Platform_Placeholders_IPlaceholderViewRequest.htm).  
[PlaceholderViewRequest](T_Tessa_Platform_Placeholders_PlaceholderViewRequest.htm)|
Запрос к представлению, который строится по плейсхолдеру.  
[PlaceholderViewRequestParameter](T_Tessa_Platform_Placeholders_PlaceholderViewRequestParameter.htm)|
Параметре для запроса к представлению, который строится по плейсхолдеру.  
[QRCodePlaceholderFormatter](T_Tessa_Platform_Placeholders_QRCodePlaceholderFormatter.htm)|
Объект, выполняющий форматирование значения поля из строки в текстовый QR-код,
представленный в виде изображения в формате PNG.
Пример: {fv:Content:#qrcode}
Пример: {fv:Content:#qrcode(w=100;h=100;px=10;t=url;ecc=q;utf8;bom)}  
[ReplacePlaceholderParser](T_Tessa_Platform_Placeholders_ReplacePlaceholderParser.htm)|
Выполняет функцию, расположенную в контексте
[IPlaceholderContext](T_Tessa_Platform_Placeholders_IPlaceholderContext.htm)
по ключу
[ReplaceFuncKey](F_Tessa_Platform_Placeholders_PlaceholderHelper_ReplaceFuncKey.htm)
и возвращающую строку с заменой плейсхолдера или null, если плейсхолдер нельзя
заменить.  
[StringPlaceholderDocument](T_Tessa_Platform_Placeholders_StringPlaceholderDocument.htm)|
Объект, определяющий способы хранения и изменения текста с заменяемыми
плейсхолдерами для строки
[String](https://learn.microsoft.com/dotnet/api/system.string).  
[StringPlaceholderDocument.MatchInfo](T_Tessa_Platform_Placeholders_StringPlaceholderDocument_MatchInfo.htm)|
Группа _group или отдельная строка _row.  
[StringPlaceholderDocumentGroup](T_Tessa_Platform_Placeholders_StringPlaceholderDocumentGroup.htm)|
Группа в текстовом документе.  
[StringPlaceholderDocumentGroupParser](T_Tessa_Platform_Placeholders_StringPlaceholderDocumentGroupParser.htm)|
Объект, который занимается построением структуры групп по тексту документа.  
[StringWithScriptsPlaceholderDocument](T_Tessa_Platform_Placeholders_StringWithScriptsPlaceholderDocument.htm)|
Объект, определяющий способы хранения и изменения текста с заменяемыми
плейсхолдерами для строки
[String](https://learn.microsoft.com/dotnet/api/system.string). Поддерживает
скрипты.  
[TablePlaceholderContext](T_Tessa_Platform_Placeholders_TablePlaceholderContext.htm)|
Часть контекста операции, связанная с плейсхолдерами для таблиц
[ITablePlaceholderType](T_Tessa_Platform_Placeholders_ITablePlaceholderType.htm).  
[TablePlaceholderReplacer](T_Tessa_Platform_Placeholders_TablePlaceholderReplacer.htm)|
Базовый класс для объекта, выполняющего замену плейсхолдера определённого
типа, работающего в режиме "таблица".  
[TablePlaceholderReplacerNames](T_Tessa_Platform_Placeholders_TablePlaceholderReplacerNames.htm)|
Название объекта, зарегистрированного по интерфейсу
[ITablePlaceholderReplacer](T_Tessa_Platform_Placeholders_ITablePlaceholderReplacer.htm).  
[TablePlaceholderType](T_Tessa_Platform_Placeholders_TablePlaceholderType.htm)|
Тип плейсхолдера, предоставляющего данные для таблицы.  
[TaskFieldPlaceholderReplacer](T_Tessa_Platform_Placeholders_TaskFieldPlaceholderReplacer.htm)|
Объект, выполняющий замену плейсхолдера типа {task:...}, работающего в режиме
"поле".  
[TextPlaceholderDocument](T_Tessa_Platform_Placeholders_TextPlaceholderDocument.htm)|
Объект, определяющий способы хранения и изменения текста с заменяемыми
плейсхолдерами для строки
[String](https://learn.microsoft.com/dotnet/api/system.string).  
[TextPlaceholderFormatter](T_Tessa_Platform_Placeholders_TextPlaceholderFormatter.htm)|
Объект, выполняющий форматирование значения поля из массива байт в строку
текста в заданной кодировке. Если плейсхолдер получает на входе строку вместо
массива байт, то он возвращает её же.
Пример: {fv:Content:#text(t=utf-16)}  
[UnknownPlaceholderParser](T_Tessa_Platform_Placeholders_UnknownPlaceholderParser.htm)|  
[ViewFieldPlaceholderReplacer](T_Tessa_Platform_Placeholders_ViewFieldPlaceholderReplacer.htm)|
Объект, выполняющий замену плейсхолдера типа {fv:...}, обращающегося к
представлению и работающего в режиме "поле".  
[ViewPlaceholderContext](T_Tessa_Platform_Placeholders_ViewPlaceholderContext.htm)|
Часть контекста операции, связанная с плейсхолдерами для представлений.  
[ViewPlaceholderInfo](T_Tessa_Platform_Placeholders_ViewPlaceholderInfo.htm)|
Информация по представлению, выполняемому из плейсхолдеров.  
[ViewTablePlaceholderReplacer](T_Tessa_Platform_Placeholders_ViewTablePlaceholderReplacer.htm)|
Объект, выполняющий замену плейсхолдера типа {tv:...}, обращающегося к
представлению и работающего в режиме "таблица".  
[WebCardLinkPlaceholderFormatter](T_Tessa_Platform_Placeholders_WebCardLinkPlaceholderFormatter.htm)|
Заменяет уникальный идентификатор на ссылку на карточку с этим идентификатором
для web-клиента.  
[WrapPlaceholderFormatter](T_Tessa_Platform_Placeholders_WrapPlaceholderFormatter.htm)|
Объект, выполняющий разбиение текста по строкам с выравниванием. При
превышении лимита производит перенос текста на следующую строку.
Пример: {f:DocumentCommonInfo.Subject:#wrap(left=16)}
Допустимы значения переноса: left, right, center.  
[WrapPlaceholderInfo](T_Tessa_Platform_Placeholders_WrapPlaceholderInfo.htm)|  
## __Структуры
[PlaceholderField](T_Tessa_Platform_Placeholders_PlaceholderField.htm)|
Значение поля в строке таблицы
[IPlaceholderRow](T_Tessa_Platform_Placeholders_IPlaceholderRow.htm) при
замене плейсхолдеров, работающих в режиме "таблица", или любая строка при
замене плейсхолдеров, работающих в "режиме поля".  
---|---  
## __Интерфейсы
[IAliasPlaceholderContext](T_Tessa_Platform_Placeholders_IAliasPlaceholderContext.htm)|
Часть контекста операции, содержащая информацию по алиасам плейсхолдеров.  
---|---  
[IAliasPlaceholderReplacer](T_Tessa_Platform_Placeholders_IAliasPlaceholderReplacer.htm)|
Объект, выполняющий замену плейсхолдера определённого типа, работающего в
режиме "замена по алиасу".  
[IAliasPlaceholderType](T_Tessa_Platform_Placeholders_IAliasPlaceholderType.htm)|
Тип плейсхолдера, определяющего замену для плейсхолдера по алиасу.  
[IDefinitionPlaceholderType](T_Tessa_Platform_Placeholders_IDefinitionPlaceholderType.htm)|
Тип плейсхолдера для установки плейсхолдеру алиаса. Используют режим замены
[Definition](T_Tessa_Platform_Placeholders_PlaceholderMode.htm) Сами такие
плейсхолдеры всегда заменяются на
[Empty](https://learn.microsoft.com/dotnet/api/system.string.empty).  
[IEditablePlaceholderTable](T_Tessa_Platform_Placeholders_IEditablePlaceholderTable.htm)|
Редактируемая таблица с данными плейсхолдера таблиц
[ITablePlaceholderType](T_Tessa_Platform_Placeholders_ITablePlaceholderType.htm).  
[IFieldPlaceholderReplacer](T_Tessa_Platform_Placeholders_IFieldPlaceholderReplacer.htm)|
Объект, выполняющий замену плейсхолдера определённого типа, работающего в
режиме "поле".  
[IFieldPlaceholderType](T_Tessa_Platform_Placeholders_IFieldPlaceholderType.htm)|
Тип плейсхолдера с режимом работы "поле"
[Field](T_Tessa_Platform_Placeholders_PlaceholderMode.htm).  
[IPlaceholder](T_Tessa_Platform_Placeholders_IPlaceholder.htm)|  Информация по
распознанному плейсхолдеру.  
[IPlaceholderCollection](T_Tessa_Platform_Placeholders_IPlaceholderCollection.htm)|
Коллекция объектов
[IPlaceholder](T_Tessa_Platform_Placeholders_IPlaceholder.htm).  
[IPlaceholderContainer](T_Tessa_Platform_Placeholders_IPlaceholderContainer.htm)|
Контейнер, содержащий регистрации типов плейсхолдеров.  
[IPlaceholderContext](T_Tessa_Platform_Placeholders_IPlaceholderContext.htm)|
Контекст операции, связанной с плейсхолдерами.  
[IPlaceholderCustomFormat](T_Tessa_Platform_Placeholders_IPlaceholderCustomFormat.htm)|
Настройки нестандартного форматирования.  
[IPlaceholderCustomFormatParser](T_Tessa_Platform_Placeholders_IPlaceholderCustomFormatParser.htm)|
Объект, выполняющий разбор настроек нестандартного форматирования по строке.  
[IPlaceholderDocument](T_Tessa_Platform_Placeholders_IPlaceholderDocument.htm)|
Объект, определяющий способы хранения и изменения текста с заменяемыми
плейсхолдерами.  
[IPlaceholderExecutableQuery](T_Tessa_Platform_Placeholders_IPlaceholderExecutableQuery.htm)|
Запрос плейсхолдера к базе данных, подготовленный для выполнения.  
[IPlaceholderExtension](T_Tessa_Platform_Placeholders_IPlaceholderExtension.htm)|
Расширение для плейсхолдеров в карточке.  
[IPlaceholderFindingContext](T_Tessa_Platform_Placeholders_IPlaceholderFindingContext.htm)|
Контекст операции, связанной с поиском и распознанием плейсхолдеров.  
[IPlaceholderFormatRequest](T_Tessa_Platform_Placeholders_IPlaceholderFormatRequest.htm)|
Запрос на выполнение форматирования для значения плейсхолдера.  
[IPlaceholderFormatResult](T_Tessa_Platform_Placeholders_IPlaceholderFormatResult.htm)|
Результат выполненного форматирования для поля или набора полей.  
[IPlaceholderFormatSettings](T_Tessa_Platform_Placeholders_IPlaceholderFormatSettings.htm)|
Настройки форматирования для вывода значений.  
[IPlaceholderFormatter](T_Tessa_Platform_Placeholders_IPlaceholderFormatter.htm)|
Объект, выполняющий форматирование значений для плейсхолдеров.  
[IPlaceholderFormatterContainer](T_Tessa_Platform_Placeholders_IPlaceholderFormatterContainer.htm)|
Контейнер, содержащий регистрации, выполняющих нестандартное форматирование
значений для плейсхолдеров.  
[IPlaceholderGroup](T_Tessa_Platform_Placeholders_IPlaceholderGroup.htm)|
Группа плейсхолдеров, определяющих группировку таблицы
[IPlaceholderTable](T_Tessa_Platform_Placeholders_IPlaceholderTable.htm)  
[IPlaceholderGroupCollection](T_Tessa_Platform_Placeholders_IPlaceholderGroupCollection.htm)|
Коллекция объектов
[IPlaceholderGroup](T_Tessa_Platform_Placeholders_IPlaceholderGroup.htm),
используемых для группировки строк в таблицах
[IPlaceholderTable](T_Tessa_Platform_Placeholders_IPlaceholderTable.htm).  
[IPlaceholderGrouping](T_Tessa_Platform_Placeholders_IPlaceholderGrouping.htm)|
Объект с информацией по группировки данных в таблице, строки которой
наполняются через плейсхолдер в режиме "таблица".  
[IPlaceholderGroupingCollection](T_Tessa_Platform_Placeholders_IPlaceholderGroupingCollection.htm)|
Коллекция объектов
[IPlaceholderGrouping](T_Tessa_Platform_Placeholders_IPlaceholderGrouping.htm),
используемых для группировки строк в таблицах в запросах плейсхолдеров к базе
данных или к другим внешним источникам данных (таким как представления).  
[IPlaceholderImageParameters](T_Tessa_Platform_Placeholders_IPlaceholderImageParameters.htm)|
Параметры, связанные с выводом плейсхолдеров-изображений.  
[IPlaceholderJoin](T_Tessa_Platform_Placeholders_IPlaceholderJoin.htm)|
Объект с информацией по объединению таблиц, который строится по плейсхолдеру.
Обычно соответствует выражению: -(Join)->Section.Field. Свойство
[Join](P_Tessa_Platform_Placeholders_IPlaceholderJoin_Join.htm) равно null для
первого элемента в списке и не равно null для всех прочих.  
[IPlaceholderJoinCollection](T_Tessa_Platform_Placeholders_IPlaceholderJoinCollection.htm)|
Коллекция объектов
[IPlaceholderJoin](T_Tessa_Platform_Placeholders_IPlaceholderJoin.htm),
используемых для объединения таблиц в запросах плейсхолдеров к базе данных.  
[IPlaceholderManager](T_Tessa_Platform_Placeholders_IPlaceholderManager.htm)|
Объект, управляющий операциями с плейсхолдерами.  
[IPlaceholderParser](T_Tessa_Platform_Placeholders_IPlaceholderParser.htm)|
Объект, выполняющий распознание найденного в документе плейсхолдера.  
[IPlaceholderQuery](T_Tessa_Platform_Placeholders_IPlaceholderQuery.htm)|
Запрос к базе данных, который строится по плейсхолдеру.  
[IPlaceholderQueryBuilder](T_Tessa_Platform_Placeholders_IPlaceholderQueryBuilder.htm)|
Объект, выполняющий формирование текста запроса по объекту
[IPlaceholderQuery](T_Tessa_Platform_Placeholders_IPlaceholderQuery.htm).  
[IPlaceholderQueryExecutor](T_Tessa_Platform_Placeholders_IPlaceholderQueryExecutor.htm)|
Объект, выполняющий построение и выполнение запроса по объекту
[IPlaceholderQuery](T_Tessa_Platform_Placeholders_IPlaceholderQuery.htm).
Запрос может не выполняться на базе данных, например, если требуемые данные
содержатся в карточке.  
[IPlaceholderQueryObject](T_Tessa_Platform_Placeholders_IPlaceholderQueryObject.htm)|
Объект запроса к базе данных, который строится по плейсхолдеру.  
[IPlaceholderQueryParser](T_Tessa_Platform_Placeholders_IPlaceholderQueryParser.htm)|
Объект, выполняющий разбор выражения для запроса к базе данных.  
[IPlaceholderReplacement](T_Tessa_Platform_Placeholders_IPlaceholderReplacement.htm)|
Объект с информацией по способу замены плейсхолдера.  
[IPlaceholderReplacementContext](T_Tessa_Platform_Placeholders_IPlaceholderReplacementContext.htm)|
Контекст операции, связанной с заменой плейсхолдеров.  
[IPlaceholderRow](T_Tessa_Platform_Placeholders_IPlaceholderRow.htm)|  Строка
с данными для плейсхолдера таблиц
[ITablePlaceholderType](T_Tessa_Platform_Placeholders_ITablePlaceholderType.htm).  
[IPlaceholderSorting](T_Tessa_Platform_Placeholders_IPlaceholderSorting.htm)|
Объект с информацией по сортировке результатов запроса, который строится по
плейсхолдеру.  
[IPlaceholderSortingCollection](T_Tessa_Platform_Placeholders_IPlaceholderSortingCollection.htm)|
Коллекция объектов
[IPlaceholderSorting](T_Tessa_Platform_Placeholders_IPlaceholderSorting.htm),
используемых для сортировки результатов в запросах плейсхолдеров к базе
данных.  
[IPlaceholderTable](T_Tessa_Platform_Placeholders_IPlaceholderTable.htm)|
Таблица с данными плейсхолдера таблиц
[ITablePlaceholderType](T_Tessa_Platform_Placeholders_ITablePlaceholderType.htm).  
[IPlaceholderText](T_Tessa_Platform_Placeholders_IPlaceholderText.htm)|
Информация по плейсхолдеру, найденная в документе.  
[IPlaceholderType](T_Tessa_Platform_Placeholders_IPlaceholderType.htm)|  Тип
плейсхолдера.  
[IPlaceholderValueTypeRegistry](T_Tessa_Platform_Placeholders_IPlaceholderValueTypeRegistry.htm)|
Реестр типов значений плейсхолдеров
[PlaceholderValueType](T_Tessa_Platform_Placeholders_PlaceholderValueType.htm).  
[IPlaceholderViewExecutor](T_Tessa_Platform_Placeholders_IPlaceholderViewExecutor.htm)|
Объект, выполняющий построение и выполнение представления по запросу
[IPlaceholderViewRequest](T_Tessa_Platform_Placeholders_IPlaceholderViewRequest.htm).  
[IPlaceholderViewParser](T_Tessa_Platform_Placeholders_IPlaceholderViewParser.htm)|
Объект, выполняющий разбор выражения для запроса к представлению.  
[IPlaceholderViewRequest](T_Tessa_Platform_Placeholders_IPlaceholderViewRequest.htm)|
Запрос к представлению, который строится по плейсхолдеру.  
[IPlaceholderViewRequestParameter](T_Tessa_Platform_Placeholders_IPlaceholderViewRequestParameter.htm)|
Параметре для запроса к представлению, который строится по плейсхолдеру.  
[ITablePlaceholderContext](T_Tessa_Platform_Placeholders_ITablePlaceholderContext.htm)|
Часть контекста операции, связанная с плейсхолдерами для таблиц
[ITablePlaceholderType](T_Tessa_Platform_Placeholders_ITablePlaceholderType.htm).  
[ITablePlaceholderReplacer](T_Tessa_Platform_Placeholders_ITablePlaceholderReplacer.htm)|
Объект, выполняющий замену плейсхолдера определённого типа, работающего в
режиме "таблица".  
[ITablePlaceholderType](T_Tessa_Platform_Placeholders_ITablePlaceholderType.htm)|
Тип плейсхолдера, предоставляющего данные для таблицы.  
[IViewPlaceholderContext](T_Tessa_Platform_Placeholders_IViewPlaceholderContext.htm)|
Часть контекста операции, связанная с плейсхолдерами для представлений.  
[IViewPlaceholderInfo](T_Tessa_Platform_Placeholders_IViewPlaceholderInfo.htm)|
Информация по представлению, выполняемому из плейсхолдеров.  
## __Делегаты
[CreateAliasPlaceholderContextFuncAsync](T_Tessa_Platform_Placeholders_CreateAliasPlaceholderContextFuncAsync.htm)|
Функция, создающая часть контекста операции, содержащую информацию по алиасам
плейсхолдеров.  
---|---  
[CreatePlaceholderEditableTableFunc](T_Tessa_Platform_Placeholders_CreatePlaceholderEditableTableFunc.htm)|
Создаёт редактируемую таблицу с данными плейсхолдеров по заданному имени name
для использования в контексте context.  
[CreateTablePlaceholderContextFuncAsync](T_Tessa_Platform_Placeholders_CreateTablePlaceholderContextFuncAsync.htm)|
Функция, создающая часть контекста операции, связанную с плейсхолдерами
таблиц.  
[CreateViewPlaceholderContextFuncAsync](T_Tessa_Platform_Placeholders_CreateViewPlaceholderContextFuncAsync.htm)|
Функция, создающая часть контекста операции, связанную с плейсхолдерами
представлений.  
[GetPlaceholderValueFunc<T>](T_Tessa_Platform_Placeholders_GetPlaceholderValueFunc_1.htm)|
Метод, возвращающий значение для операции с плейсхолдером.  
[PlaceholderReplaceFuncAsync](T_Tessa_Platform_Placeholders_PlaceholderReplaceFuncAsync.htm)|
Функция, которая заменяет плейсхолдер данного типа на возвращаемую строку.
Возвращает null, если замену провести невозможно. Возвращает пустую строку,
если плейсхолдер всегда должен быть заменён на пустую строку.  
## __Перечисления
[BarcodePlaceholderLabelType](T_Tessa_Platform_Placeholders_BarcodePlaceholderLabelType.htm)|
Расположение метки с текстом штрих-кода, который выводится рядом с
изображением.  
---|---  
[FindingOptions](T_Tessa_Platform_Placeholders_FindingOptions.htm)|  Опции по
поиску и распознанию плейсхолдеров.  
[PlaceholderFieldFlags](T_Tessa_Platform_Placeholders_PlaceholderFieldFlags.htm)|
Флаги, связанные со значением
[PlaceholderField](T_Tessa_Platform_Placeholders_PlaceholderField.htm).  
[PlaceholderMode](T_Tessa_Platform_Placeholders_PlaceholderMode.htm)|  Режим
работы плейсхолдера.  
[PlaceholderQueryBuilderFlags](T_Tessa_Platform_Placeholders_PlaceholderQueryBuilderFlags.htm)|
Флаги, влияющие на формирование текста запроса по объекту
[IPlaceholderQuery](T_Tessa_Platform_Placeholders_IPlaceholderQuery.htm).  
[QRCodePlaceholderType](T_Tessa_Platform_Placeholders_QRCodePlaceholderType.htm)|
Тип QR-кода для вывода в плейсхолдерах.  
[ReplacementOptions](T_Tessa_Platform_Placeholders_ReplacementOptions.htm)|
Опции по замене плейсхолдеров.  
[StringPlaceholderDocumentGroupType](T_Tessa_Platform_Placeholders_StringPlaceholderDocumentGroupType.htm)|  
[ViewRequestParameterSourceType](T_Tessa_Platform_Placeholders_ViewRequestParameterSourceType.htm)|
Тип источника данных для параметра запроса к представлению.  
[WrapPlaceholderAlignment](T_Tessa_Platform_Placeholders_WrapPlaceholderAlignment.htm)|
Выравнивание текста в плейсхолдерах при переносе.
