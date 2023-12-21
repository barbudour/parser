# CardExtensions - методы
##  __Методы
[AddCardTypeInfoToSections](M_Tessa_Cards_CardExtensions_AddCardTypeInfoToSections.htm)|
Добавляет информацию по типу карточки cardTypeID для колонок в метаинформации
sections, которые перечислены в schemeItem, если этого типа ещё нет в
соответствующих колонках. Возвращает признак того, что метод внёс изменения в
метаинформацию.  
---|---  
[AddDistinctFrom(ICollection<CardTypeSchemeItem>,
ICollection<CardTypeSchemeItem>)](M_Tessa_Cards_CardExtensions_AddDistinctFrom.htm)|
Добавляет элементы схемы в текущую коллекцию из заданной коллекции
schemeItems, если таких же элементов уже не было в текущей коллекции.
Возвращает признак того, что хотя бы одна секция или колонка была добавлена.  
[AddDistinctFrom(ICollection<CardTypeSchemeItem>,
ICollection<CardTypeSchemeItem>, CardMetadataSectionCollection,
Guid)](M_Tessa_Cards_CardExtensions_AddDistinctFrom_1.htm)|  Добавляет
элементы схемы в текущую коллекцию из заданной коллекции schemeItems, если
таких же элементов уже не было в текущей коллекции. Возвращает признак того,
что хотя бы одна секция или колонка была добавлена. Метод также добавляет в
колонки секций sections информацию по типу карточки cardTypeID. В расширениях
на метаинформации используйте эту перегрузку метода только в
[ModifyMetadata(ICardMetadataExtensionContext)](M_Tessa_Cards_Extensions_ICardMetadataExtension_ModifyMetadata.htm).  
[AddInstanceNotFoundError](M_Tessa_Cards_CardExtensions_AddInstanceNotFoundError.htm)|
Добавляет ошибку валидации
[InstanceNotFound](F_Tessa_Cards_CardValidationKeys_InstanceNotFound.htm) с
информацией по стеку вызовов, если это разрешено флагами flags.  
[AppliesRequiredToControl](M_Tessa_Cards_CardExtensions_AppliesRequiredToControl.htm)|
Возвращает признак того, что валидатор устанавливает признак "Обязательно для
заполнения" для заданного элемента управления control.  
[ApplyFromAsync](M_Tessa_Cards_CardExtensions_ApplyFromAsync.htm)|
Устанавливает разрешения, связанные с контейнером файлов, по разрешениям,
заданным в карточке.  
[ApplyUserSettingsToRolesAsync](M_Tessa_Cards_CardExtensions_ApplyUserSettingsToRolesAsync.htm)|
Асинхронно выполняет копирование настроек одного сотрудника на заданный список
ролей (без учёта заместителей). Запрос доступен только для администраторов.
Возвращает сообщения валидации, в т.ч. возникшие ошибки. Возвращаемое значение
не равно null.  
[ChangePasswordForCurrentUserAsync](M_Tessa_Cards_CardExtensions_ChangePasswordForCurrentUserAsync.htm)|
Асинхронно изменяет пароль для текущего сотрудника, если у него тип входа
"Пользователь Tessa". Возвращает сообщения валидации, в т.ч. возникшие ошибки.
Возвращаемое значение не равно null.  
[CopyAndAddRange<T>](M_Tessa_Cards_CardExtensions_CopyAndAddRange__1.htm)|
Копирует коллекцию сериализуемых объектов sourceItems и в конец коллекции
сериализуемых объектов targetItems. Устанавливает порядок следования объектов,
если объекты поддерживают
[ICardMetadataOrderable](T_Tessa_Cards_ICardMetadataOrderable.htm).  
[CopyAndInsert<T>](M_Tessa_Cards_CardExtensions_CopyAndInsert__1.htm)|
Копирует коллекцию сериализуемых объектов sourceItems и вставляет по индексу в
коллекцию сериализуемых объектов targetItems. Устанавливает порядок следования
объектов, если объекты поддерживают
[ICardMetadataOrderable](T_Tessa_Cards_ICardMetadataOrderable.htm).  
[CopyToTheBeginningOf<T>](M_Tessa_Cards_CardExtensions_CopyToTheBeginningOf__1.htm)|
Копирует коллекцию сериализуемых объектов sourceItems в начало коллекции
сериализуемых объектов targetItems. Устанавливает порядок следования объектов,
если объекты поддерживают
[ICardMetadataOrderable](T_Tessa_Cards_ICardMetadataOrderable.htm).  
[CreateContainerRemoteAsync](M_Tessa_Cards_CardExtensions_CreateContainerRemoteAsync.htm)|
Создаёт контейнер с информацией по заданной карточке и по её файлам. Все файлы
создаются с Remote-содержимым, при загрузке и замене которого не используется
временная папка. Операции с такими файлами будут выполняться быстрее, но при
условии надо быть уверенными, что содержимое файлов, работа с которыми
выполняется, умещается в памяти. Возможные ошибки при загрузке файлов из
карточки игнорируются. В этом случае к созданном контейнере не будет добавлено
файлов, хотя файлы присутствуют в карточке.  
[DeepClone(CardTypeControl)](M_Tessa_Cards_CardExtensions_DeepClone.htm)|
Выполняет глубокое клонирование метаинформации по элементу управления
[CardTypeControl](T_Tessa_Cards_CardTypeControl.htm) за счёт его полной
сериализации / десериализации.  
[DeepClone<T>(T)](M_Tessa_Cards_CardExtensions_DeepClone__1.htm)|  Выполняет
глубокое клонирование сериализуемого объекта за счёт его полной сериализации /
десериализации.  
[DeleteAsync(ICardTypeClientRepository, CardType,
CancellationToken)](M_Tessa_Cards_CardExtensions_DeleteAsync.htm)|  Удаляет
заданный тип карточки.  
[DeleteAsync(ICardTypeServerRepository, ICardSerializableEntry,
CancellationToken)](M_Tessa_Cards_CardExtensions_DeleteAsync_1.htm)|  Удаляет
заданный тип карточки.  
[DeleteAsync(ICardTypeService, ICardSerializableEntry,
CancellationToken)](M_Tessa_Cards_CardExtensions_DeleteAsync_2.htm)|  Удаляет
заданный тип карточки.  
[DeserializeFromJson<T>](M_Tessa_Cards_CardExtensions_DeserializeFromJson__1.htm)|
Десериализует объект и его дочерние объекты из заданного текстового JSON с
сохраняемыми типами данных.  
[DeserializeFromStorage<T>](M_Tessa_Cards_CardExtensions_DeserializeFromStorage__1.htm)|
Десериализует объект из заданного хранилища Dictionary<string, object>.  
[GenerateExportAsync](M_Tessa_Cards_CardExtensions_GenerateExportAsync.htm)|
Создаёт файл по заданному шаблону и возвращает контент созданного файла и
ответ на запрос на создание.  
[GenerateFileFromTemplateAsync(ICardStreamServerRepository, Guid,
Nullable<Guid>, IViewPlaceholderContext, Dictionary<String, Object>,
CancellationToken)](M_Tessa_Cards_CardExtensions_GenerateFileFromTemplateAsync_1.htm)|
Асинхронно создаёт файл по заданному шаблону и возвращает контент созданного
файла и ответ на запрос на создание.  
[GenerateFileFromTemplateAsync(ICardStreamClientRepository, Guid,
Nullable<Guid>, Func<Stream, CancellationToken, ValueTask>,
IViewPlaceholderContext, Dictionary<String, Object>,
CancellationToken)](M_Tessa_Cards_CardExtensions_GenerateFileFromTemplateAsync.htm)|
Создаёт файл по заданному шаблону и возвращает контент созданного файла и
ответ на запрос на создание.  
[GetAllCardTypeCollectionAsync](M_Tessa_Cards_CardExtensions_GetAllCardTypeCollectionAsync.htm)|
Возвращает коллекцию, содержащую все типы карточек.  
[GetDigestAsync](M_Tessa_Cards_CardExtensions_GetDigestAsync.htm)|  Асинхронно
возвращает Digest для заданной карточки, полученный выполнением запроса
[GetDigest](F_Tessa_Cards_CardRequestTypes_GetDigest.htm), или null, если
Digest неизвестен или не требуется.  
[GetEntryPermissions](M_Tessa_Cards_CardExtensions_GetEntryPermissions.htm)|
Возвращает права доступа к полям строковой секции с именем sectionName.  
[GetFieldNames](M_Tessa_Cards_CardExtensions_GetFieldNames.htm)|  Возвращает
имена полей, с которыми связан контрол
[CardTypeEntryControl](T_Tessa_Cards_CardTypeEntryControl.htm).  
[GetFileSourceAsync(ICardRepository, Card, CardFile,
CancellationToken)](M_Tessa_Cards_CardExtensions_GetFileSourceAsync_1.htm)|
Асинхронно возвращает местоположение контента файла для заданного файла file
указанной карточки card. Местоположение определяется выполнением запроса
[GetFileSource](F_Tessa_Cards_CardRequestTypes_GetFileSource.htm). Метод
возвращает null, если определить местоположение не удалось, обычно в этом
случае будет использоваться местоположение по умолчанию.  
[GetFileSourceAsync(ICardRequestComponent, Card, CardFile, ICardMetadata,
ISession,
CancellationToken)](M_Tessa_Cards_CardExtensions_GetFileSourceAsync.htm)|
Возвращает местоположение контента файла для заданного файла file указанной
карточки card. Местоположение определяется выполнением запроса
[GetFileSource](F_Tessa_Cards_CardRequestTypes_GetFileSource.htm). Метод
возвращает null, если определить местоположение не удалось, обычно в этом
случае будет использоваться местоположение по умолчанию.  
[GetID(CardTypeCompletionOption)](M_Tessa_Cards_CardExtensions_GetID.htm)|
Получить уникальный идентификатор объекта на основе хэш-кода его типа и
настроек.  
[GetID(CardTypeExtension)](M_Tessa_Cards_CardExtensions_GetID_1.htm)|
Получить уникальный идентификатор объекта на основе хэш-кода его типа и
настроек.  
[GetID(CardTypeValidator)](M_Tessa_Cards_CardExtensions_GetID_2.htm)|
Получить уникальный идентификатор объекта на основе хэш-кода его типа и
настроек.  
[GetOrAddEntry(StringDictionaryStorage<CardSection>,
String)](M_Tessa_Cards_CardExtensions_GetOrAddEntry.htm)|  Возвращает
строковую секцию с заданным именем. Если секция отсутствовала, то создаёт её.
Если требуется создать коллекционную или древовидную секцию, то используйте
метод GetOrAddTable.  
[GetOrAddEntry(StringDictionaryStorage<CardSectionPermissionInfo>,
String)](M_Tessa_Cards_CardExtensions_GetOrAddEntry_1.htm)|  Возвращает объект
с разрешениями на коллекционную или древовидную секцию с заданным именем. Если
секция отсутствовала, то создаёт её. Если требуется создать объект для
коллекционной или древовидной секции, то используйте метод GetOrAddEntry.  
[GetOrAddTable(StringDictionaryStorage<CardSectionPermissionInfo>,
String)](M_Tessa_Cards_CardExtensions_GetOrAddTable_1.htm)|  Возвращает объект
с разрешениями на коллекционную или древовидную секцию с заданным именем. Если
секция отсутствовала, то создаёт её. Если требуется создать объект для
строковой секции, то используйте метод GetOrAddEntry.  
[GetOrAddTable(StringDictionaryStorage<CardSection>, String,
CardTableType)](M_Tessa_Cards_CardExtensions_GetOrAddTable.htm)|  Возвращает
коллекционную или древовидную секцию с заданным именем. Если секция
отсутствовала, то создаёт её. Если требуется создать строковую секцию, то
используйте метод GetOrAddEntry.  
[GetSourceInfo](M_Tessa_Cards_CardExtensions_GetSourceInfo.htm)|  Метод для
поулчения информации об источнике данных контрола с учетом возможной
регистрации кастомного метода для получения источника данных в
[ICardControlTypeRegistry](T_Tessa_Cards_ICardControlTypeRegistry.htm)  
[GetTablePermissions](M_Tessa_Cards_CardExtensions_GetTablePermissions.htm)|
Возвращает права доступа к строкам коллекционной секции с именем sectionName.  
[GetTypeIDAsync](M_Tessa_Cards_CardExtensions_GetTypeIDAsync.htm)|  Асинхронно
возвращает результат выполнения запроса
[GetTypeIDList](F_Tessa_Cards_CardRequestTypes_GetTypeIDList.htm) на получение
идентификатора типа карточки по заданному идентификатору карточки. Значение
null возвращается в случае, если идентификатор типа не был определён.  
[GetTypeIDListAsync](M_Tessa_Cards_CardExtensions_GetTypeIDListAsync.htm)|
Асинхронно возвращает результат выполнения запроса
[GetTypeIDList](F_Tessa_Cards_CardRequestTypes_GetTypeIDList.htm) на получение
идентификаторов типов карточек по заданным идентификаторам карточек. Элементы
результирующего массива со значениями null возвращаются в случае, если
идентификатор типа не был определён.  
[Has(CardControlTypeFlags,
CardControlTypeFlags)](M_Tessa_Cards_CardExtensions_Has.htm)| Возвращает
признак того, что заданный флаг установлен.  
[Has(CardFileFlags, CardFileFlags)](M_Tessa_Cards_CardExtensions_Has_1.htm)|
Возвращает признак того, что заданный флаг установлен.  
[Has(CardGetRestrictionFlags,
CardGetRestrictionFlags)](M_Tessa_Cards_CardExtensions_Has_2.htm)| Возвращает
признак того, что заданный флаг установлен.  
[Has(CardPermissionFlags,
CardPermissionFlags)](M_Tessa_Cards_CardExtensions_Has_3.htm)| Возвращает
признак того, что заданный флаг установлен.  
[Has(CardTaskFlags, CardTaskFlags)](M_Tessa_Cards_CardExtensions_Has_4.htm)|
Возвращает признак того, что заданный флаг установлен.  
[Has(CardTypeColumnFlags,
CardTypeColumnFlags)](M_Tessa_Cards_CardExtensions_Has_5.htm)| Возвращает
признак того, что заданный флаг установлен.  
[Has(CardTypeCompletionOptionFlags,
CardTypeCompletionOptionFlags)](M_Tessa_Cards_CardExtensions_Has_6.htm)|
Возвращает признак того, что заданный флаг установлен.  
[Has(CardTypeCustomControlFlags,
CardTypeCustomControlFlags)](M_Tessa_Cards_CardExtensions_Has_7.htm)|
Возвращает признак того, что заданный флаг установлен.  
[Has(CardTypeEntryControlFlags,
CardTypeEntryControlFlags)](M_Tessa_Cards_CardExtensions_Has_8.htm)|
Возвращает признак того, что заданный флаг установлен.  
[Has(CardTypeFlags, CardTypeFlags)](M_Tessa_Cards_CardExtensions_Has_9.htm)|
Возвращает признак того, что заданный флаг установлен.  
[Has(CardTypeTabControlFlags,
CardTypeTabControlFlags)](M_Tessa_Cards_CardExtensions_Has_10.htm)| Возвращает
признак того, что заданный флаг установлен.  
[Has(CardTypeTableControlFlags,
CardTypeTableControlFlags)](M_Tessa_Cards_CardExtensions_Has_11.htm)|
Возвращает признак того, что заданный флаг установлен.  
[HasAny(CardControlTypeFlags,
CardControlTypeFlags)](M_Tessa_Cards_CardExtensions_HasAny.htm)| Возвращает
признак того, что один из заданных флагов установлен.  
[HasAny(CardFileFlags,
CardFileFlags)](M_Tessa_Cards_CardExtensions_HasAny_1.htm)| Возвращает признак
того, что один из заданных флагов установлен.  
[HasAny(CardGetRestrictionFlags,
CardGetRestrictionFlags)](M_Tessa_Cards_CardExtensions_HasAny_2.htm)|
Возвращает признак того, что один из заданных флагов установлен.  
[HasAny(CardPermissionFlags,
CardPermissionFlags)](M_Tessa_Cards_CardExtensions_HasAny_3.htm)| Возвращает
признак того, что один из заданных флагов установлен.  
[HasAny(CardTaskFlags,
CardTaskFlags)](M_Tessa_Cards_CardExtensions_HasAny_4.htm)| Возвращает признак
того, что один из заданных флагов установлен.  
[HasAny(CardTypeColumnFlags,
CardTypeColumnFlags)](M_Tessa_Cards_CardExtensions_HasAny_5.htm)| Возвращает
признак того, что один из заданных флагов установлен.  
[HasAny(CardTypeCompletionOptionFlags,
CardTypeCompletionOptionFlags)](M_Tessa_Cards_CardExtensions_HasAny_6.htm)|
Возвращает признак того, что один из заданных флагов установлен.  
[HasAny(CardTypeCustomControlFlags,
CardTypeCustomControlFlags)](M_Tessa_Cards_CardExtensions_HasAny_7.htm)|
Возвращает признак того, что один из заданных флагов установлен.  
[HasAny(CardTypeEntryControlFlags,
CardTypeEntryControlFlags)](M_Tessa_Cards_CardExtensions_HasAny_8.htm)|
Возвращает признак того, что один из заданных флагов установлен.  
[HasAny(CardTypeFlags,
CardTypeFlags)](M_Tessa_Cards_CardExtensions_HasAny_9.htm)| Возвращает признак
того, что один из заданных флагов установлен.  
[HasAny(CardTypeTabControlFlags,
CardTypeTabControlFlags)](M_Tessa_Cards_CardExtensions_HasAny_10.htm)|
Возвращает признак того, что один из заданных флагов установлен.  
[HasAny(CardTypeTableControlFlags,
CardTypeTableControlFlags)](M_Tessa_Cards_CardExtensions_HasAny_11.htm)|
Возвращает признак того, что один из заданных флагов установлен.  
[HasContent](M_Tessa_Cards_CardExtensions_HasContent.htm)|  Возвращает признак
того, что состояние файла в карточке обязывает предоставить для такого файла
контент, причём карточка с файлом должна сохраняться через потоковое
сохранение.  
[HasNot(CardControlTypeFlags,
CardControlTypeFlags)](M_Tessa_Cards_CardExtensions_HasNot.htm)| Возвращает
признак того, что заданный флаг не установлен.  
[HasNot(CardFileFlags,
CardFileFlags)](M_Tessa_Cards_CardExtensions_HasNot_1.htm)| Возвращает признак
того, что заданный флаг не установлен.  
[HasNot(CardGetRestrictionFlags,
CardGetRestrictionFlags)](M_Tessa_Cards_CardExtensions_HasNot_2.htm)|
Возвращает признак того, что заданный флаг не установлен.  
[HasNot(CardPermissionFlags,
CardPermissionFlags)](M_Tessa_Cards_CardExtensions_HasNot_3.htm)| Возвращает
признак того, что заданный флаг не установлен.  
[HasNot(CardTaskFlags,
CardTaskFlags)](M_Tessa_Cards_CardExtensions_HasNot_4.htm)| Возвращает признак
того, что заданный флаг не установлен.  
[HasNot(CardTypeColumnFlags,
CardTypeColumnFlags)](M_Tessa_Cards_CardExtensions_HasNot_5.htm)| Возвращает
признак того, что заданный флаг не установлен.  
[HasNot(CardTypeCompletionOptionFlags,
CardTypeCompletionOptionFlags)](M_Tessa_Cards_CardExtensions_HasNot_6.htm)|
Возвращает признак того, что заданный флаг не установлен.  
[HasNot(CardTypeCustomControlFlags,
CardTypeCustomControlFlags)](M_Tessa_Cards_CardExtensions_HasNot_7.htm)|
Возвращает признак того, что заданный флаг не установлен.  
[HasNot(CardTypeEntryControlFlags,
CardTypeEntryControlFlags)](M_Tessa_Cards_CardExtensions_HasNot_8.htm)|
Возвращает признак того, что заданный флаг не установлен.  
[HasNot(CardTypeFlags,
CardTypeFlags)](M_Tessa_Cards_CardExtensions_HasNot_9.htm)| Возвращает признак
того, что заданный флаг не установлен.  
[HasNot(CardTypeTabControlFlags,
CardTypeTabControlFlags)](M_Tessa_Cards_CardExtensions_HasNot_10.htm)|
Возвращает признак того, что заданный флаг не установлен.  
[HasNot(CardTypeTableControlFlags,
CardTypeTableControlFlags)](M_Tessa_Cards_CardExtensions_HasNot_11.htm)|
Возвращает признак того, что заданный флаг не установлен.  
[InsertWithoutCopy<T>](M_Tessa_Cards_CardExtensions_InsertWithoutCopy__1.htm)|
Вставляет коллекцию сериализуемых объектов sourceItems по указанному индексу в
коллекцию сериализуемых объектов targetItems.  
[MakeGlobal(CardTypeCompletionOption,
CardGlobalReferencesContext)](M_Tessa_Cards_CardExtensions_MakeGlobal_7.htm)|
Сделать указанный объект глобальным.  
[MakeGlobal(CardTypeExtension,
CardGlobalReferencesContext)](M_Tessa_Cards_CardExtensions_MakeGlobal_9.htm)|
Сделать указанный объект глобальным.  
[MakeGlobal(CardTypeNamedForm,
CardGlobalReferencesContext)](M_Tessa_Cards_CardExtensions_MakeGlobal_10.htm)|
Сделать указанный объект глобальным.  
[MakeGlobal(CardTypeValidator,
CardGlobalReferencesContext)](M_Tessa_Cards_CardExtensions_MakeGlobal_11.htm)|
Сделать указанный объект глобальным.  
[MakeGlobal(IEnumerable<CardTypeCompletionOption>,
CardGlobalReferencesContext)](M_Tessa_Cards_CardExtensions_MakeGlobal_1.htm)|
Сделать варианты завершения глобальными.  
[MakeGlobal(IEnumerable<CardTypeExtension>,
CardGlobalReferencesContext)](M_Tessa_Cards_CardExtensions_MakeGlobal_3.htm)|
Сделать расширения типа карточки глобальными.  
[MakeGlobal(IEnumerable<CardTypeNamedForm>,
CardGlobalReferencesContext)](M_Tessa_Cards_CardExtensions_MakeGlobal_4.htm)|
Сделать формы типа карточки глобальными.  
[MakeGlobal(IEnumerable<CardTypeValidator>,
CardGlobalReferencesContext)](M_Tessa_Cards_CardExtensions_MakeGlobal_5.htm)|
Сделать валидаторы типа карточки глобальными.  
[MakeGlobal(CardTypeBlock, CardGlobalReferencesContext,
CardSerializableObject[])](M_Tessa_Cards_CardExtensions_MakeGlobal_6.htm)|
Сделать указанный объект глобальным.  
[MakeGlobal(CardTypeControl, CardGlobalReferencesContext,
CardSerializableObject[])](M_Tessa_Cards_CardExtensions_MakeGlobal_8.htm)|
Сделать указанный объект глобальным.  
[MakeGlobal(IEnumerable<CardTypeBlock>, CardGlobalReferencesContext,
CardSerializableObject[])](M_Tessa_Cards_CardExtensions_MakeGlobal.htm)|
Сделать блоки формы типа карточки глобальными.  
[MakeGlobal(IEnumerable<CardTypeControl>, CardGlobalReferencesContext,
CardSerializableObject[])](M_Tessa_Cards_CardExtensions_MakeGlobal_2.htm)|
Сделать контролы типа карточки глобальными.  
[OrderByDependenciesAsync](M_Tessa_Cards_CardExtensions_OrderByDependenciesAsync.htm)|
Упорядочивает секции карточки с учётом зависимостей между секциями в порядке,
который необходим для выполнения запросов на вставку записей. Для удаления
записей необходим обратный порядок.  
[OrderHierarchyForDeletion<T>](M_Tessa_Cards_CardExtensions_OrderHierarchyForDeletion__1.htm)|
Упорядочивает строки таким образом, чтобы их можно было удалить из базы данных
с учётом связи между родительскими и дочерними строками.  
[OrderHierarchyForInsertion<T>](M_Tessa_Cards_CardExtensions_OrderHierarchyForInsertion__1.htm)|
Упорядочивает строки таким образом, чтобы их можно было вставить в базу данных
с учётом связи между родительскими и дочерними строками.  
[OrderManuallyForDeletion<T>](M_Tessa_Cards_CardExtensions_OrderManuallyForDeletion__1.htm)|
Упорядочивает строки таким образом, чтобы их можно было удалить из базы
данных, с учётом порядка строк по убыванию, определяемого пользователем в
свойстве [Order](P_Tessa_Cards_ICardOrderable_Order.htm) каждой строки.  
[OrderManuallyForInsertion<T>](M_Tessa_Cards_CardExtensions_OrderManuallyForInsertion__1.htm)|
Упорядочивает строки таким образом, чтобы их можно было вставить в базу
данных, с учётом порядка строк по возрастанию, определяемого пользователем в
свойстве [Order](P_Tessa_Cards_ICardOrderable_Order.htm) каждой строки.  
[RegisterCardClientComponents](M_Tessa_Cards_CardExtensions_RegisterCardClientComponents.htm)|
Выполняет регистрацию репозиториев в контейнере Unity с клиентскими
компонентами для API карточек. Все репозитории регистрируются по именам,
указанным в [CardRepositoryNames](T_Tessa_Cards_CardRepositoryNames.htm).
Регистрация репозиториев без имени не выполняется.  
[RegisterCardExtensionTypes](M_Tessa_Cards_CardExtensions_RegisterCardExtensionTypes.htm)|
Выполняет регистрацию стандартных типов расширений для карточек.  
[RegisterCardServerComponents](M_Tessa_Cards_CardExtensions_RegisterCardServerComponents.htm)|
Выполняет регистрацию репозиториев в контейнере Unity с серверными
компонентами для API карточек. Все репозитории регистрируются по именам,
указанным в [CardRepositoryNames](T_Tessa_Cards_CardRepositoryNames.htm).
Регистрация репозиториев без имени не выполняется.  
[RegisterCardsOnClient](M_Tessa_Cards_CardExtensions_RegisterCardsOnClient.htm)|
Выполняет регистрацию клиентских сервисов и объектов API карточек в контейнере
Unity. Также выполняет регистрацию компонент посредством метода
[RegisterCardClientComponents(IUnityContainer)](M_Tessa_Cards_CardExtensions_RegisterCardClientComponents.htm)
и репозиториев, которые регистрируются без имени. Не выполняет установку
файловых хранилищ, рекомендуется вызвать метод-расширение
[SetCachingSourceForFileSettings(IUnityContainer)](M_Tessa_Cards_CardExtensions_SetCachingSourceForFileSettings.htm)
при завершении регистраций на сервере.  
[RegisterCardsOnServer](M_Tessa_Cards_CardExtensions_RegisterCardsOnServer.htm)|
Выполняет регистрацию сервисов и объектов API карточек на серверной стороне в
контейнере Unity. Также выполняет регистрацию компонент посредством метода
[RegisterCardServerComponents(IUnityContainer)](M_Tessa_Cards_CardExtensions_RegisterCardServerComponents.htm)
и репозиториев, которые регистрируются без имени. Не выполняет установку
файловых хранилищ, рекомендуется вызвать метод-расширение
[SetCachingSourceForFileSettings(IUnityContainer)](M_Tessa_Cards_CardExtensions_SetCachingSourceForFileSettings.htm)
при завершении регистраций на сервере.  
[RegisterCardTraceListeners](M_Tessa_Cards_CardExtensions_RegisterCardTraceListeners.htm)|
Выполняет регистрацию объектов, отслеживающих события, происходящие при
выполнении расширений карточек, и записывающие результат выполнения в
[ValidationResult](P_Tessa_Extensions_ITraceableExtensionContext_ValidationResult.htm)
как информационное сообщение. Это полезно при отладке расширений, но сильно
нагружает любое взаимодействие с карточками, поэтому рекомендуется не
выполнять такую регистрацию в среде, с которой работают конечные пользователи.  
[RemoveCardTraceListeners](M_Tessa_Cards_CardExtensions_RemoveCardTraceListeners.htm)|
Удаляет объекты, зарегистрированные методом
[RegisterCardTraceListeners(IExtensionContainer, ExtensionTraceListenerType,
Nullable<Int64>)](M_Tessa_Cards_CardExtensions_RegisterCardTraceListeners.htm).
Частая регистрация с последующим удалением объектов значительно нагружает
память и CPU.  
[RepairAsync](M_Tessa_Cards_CardExtensions_RepairAsync.htm)|  Выполняет
исправление структуры заданной карточки на основании данных в контексте
расширений по исправлению карточки. Метод полезен для исправления карточек-
сателлитов, связанных с основной исправляемой карточкой. После исправления
любые сообщения будут записаны в результат валидации текущего контекста.
Возвращает признак того, что исправление выполнено успешно, т.е. без ошибок,
предотвращающих использование карточки.  
[ReplaceBlocks(CardTypeForm,
CardTypeForm)](M_Tessa_Cards_CardExtensions_ReplaceBlocks_1.htm)|  Заменить
блоки формы на блоки исходной формы.  
[ReplaceBlocks(IEnumerable<CardTypeForm>,
IEnumerable<CardTypeForm>)](M_Tessa_Cards_CardExtensions_ReplaceBlocks.htm)|
Заменить все блоки указанных форм на блоки переданных форм.  
[ReplaceControls(CardTypeBlock,
CardTypeBlock)](M_Tessa_Cards_CardExtensions_ReplaceControls_1.htm)|  Заменить
контролы блока на контролы исходного блока.  
[ReplaceControls(IEnumerable<CardTypeBlock>,
IEnumerable<CardTypeBlock>)](M_Tessa_Cards_CardExtensions_ReplaceControls.htm)|
Заменить все контролы указанных блоков на контролы переданных блоков.  
[SetCachingSourceForFileSettings](M_Tessa_Cards_CardExtensions_SetCachingSourceForFileSettings.htm)|
Устанавливает в качестве источника настроек
[ICardCache](T_Tessa_Cards_Caching_ICardCache.htm) для зарегистрированного
объекта [ICardFileSourceSettings](T_Tessa_Cards_ICardFileSourceSettings.htm).
Привязывает кэш к параметрам лицензии
[ILicenseManager](T_Tessa_Platform_Licensing_ILicenseManager.htm), если этот
объект зарегистрирован. Не выполняет действий, если хотя бы одна из
зависимостей [ICardCache](T_Tessa_Cards_Caching_ICardCache.htm) или
[ICardFileSourceSettings](T_Tessa_Cards_ICardFileSourceSettings.htm) не
зарегистрированы.  
[SetNormalized](M_Tessa_Cards_CardExtensions_SetNormalized.htm)|
Устанавливает заданные флаги с учётом нормализации. При указании флага flag
как Allow автоматически сбрасывает соответствующий флаг Prohibit, и наоборот.
Результат применяется к flags и возвращается в результате метода.  
[StoreAsync](M_Tessa_Cards_CardExtensions_StoreAsync.htm)|  Сохраняет карточку
из текущего контейнера и контент её файлов, при этом позволяет асинхронно
отслеживать её состояние. В процессе сохранения карточка в контейнере и её
файлы не изменяются, поэтому метод безопасно вызывать повторно.  
[ToCardTableType](M_Tessa_Cards_CardExtensions_ToCardTableType.htm)|
Преобразует перечисление значение перечисления
[SchemeTableContentType](T_Tessa_Scheme_SchemeTableContentType.htm) к типу
[CardTableType](T_Tessa_Cards_CardTableType.htm).  
[ToDictionary](M_Tessa_Cards_CardExtensions_ToDictionary.htm)|  Создаёт хеш-
таблицу, позволяющую быстро получить доступ к строкам коллекционных и
древовидных секций по имени секции. Строки
[CardRow](T_Tessa_Cards_CardRow.htm) не копируются.  
[ToStringDictionaryStorage](M_Tessa_Cards_CardExtensions_ToStringDictionaryStorage.htm)|
Создаёт объект StringDictionaryStorage<CardRow> по заданной хеш-таблице,
позволяющей получить доступ к строкам коллекционных и древовидных секций по
имени секции. Строки [CardRow](T_Tessa_Cards_CardRow.htm) копируются.  
[TryAddTaskAsync](M_Tessa_Cards_CardExtensions_TryAddTaskAsync.htm)|  Создаёт
и добавляет возвращаемое задание с заданными параметрами. После создания может
потребоваться заполнить секции задания и другие параметры
[CardTask](T_Tessa_Cards_CardTask.htm). Возвращённый объект
[ValidationResult](T_Tessa_Platform_Validation_ValidationResult.htm) содержит
ошибки и сообщения, возникшие при создании задания, он всегда не равен null.
Возвращённый объект [CardTask](T_Tessa_Cards_CardTask.htm) может быть равен
null, если при создании были ошибки. В этом случае возвращённый объект
[ValidationResult](T_Tessa_Platform_Validation_ValidationResult.htm) содержит
эти ошибки.  
[TryGetFieldIgnoreCaseAsync<T>](M_Tessa_Cards_CardExtensions_TryGetFieldIgnoreCaseAsync__1.htm)|
Возвращает значение поля строковой секции или строки коллекционной секции
карточки без учёта регистра или null, если такое поле отсутствует.  
[TryGetIgnoreCase(CardMetadataSectionCollection,
String)](M_Tessa_Cards_CardExtensions_TryGetIgnoreCase_1.htm)|  Возвращает
секцию из метаинформации, полученную без учёта регистра, или null, если такая
секция отсутствует.  
[TryGetIgnoreCase(CardMetadataColumnCollection, String,
Boolean)](M_Tessa_Cards_CardExtensions_TryGetIgnoreCase.htm)|  Возвращает
колонку из метаинформации, полученную без учёта регистра, или null, если такая
колонка отсутствует.  
[TryGetIgnoreCaseAsync(StringDictionaryStorage<CardSection>, String,
ICardMetadata,
CancellationToken)](M_Tessa_Cards_CardExtensions_TryGetIgnoreCaseAsync.htm)|
Возвращает секцию карточки, полученную без учёта регистра, или null, если
такая секция отсутствует.  
[TryGetIgnoreCaseAsync(StringDictionaryStorage<CardSectionPermissionInfo>,
String, ICardMetadata,
CancellationToken)](M_Tessa_Cards_CardExtensions_TryGetIgnoreCaseAsync_1.htm)|
Возвращает разрешения для секции карточки, полученной без учёта регистра, или
null, если такая секция отсутствует.  
[TrySetFieldIgnoreCaseAsync](M_Tessa_Cards_CardExtensions_TrySetFieldIgnoreCaseAsync.htm)|
Устанавливает значение поля строковой секции или строки коллекционной секции
карточки без учёта регистра. Возвращает признак того, что значение было
установлено, т.к. было определено имя поля с учётом регистра.  
[UsedIn](M_Tessa_Cards_CardExtensions_UsedIn.htm)|  Возвращает признак того,
что флаги элемента управления позволяют ему располагаться в карточках с
заданным типом экземпляра.  
[WhenAnyCardType](M_Tessa_Cards_CardExtensions_WhenAnyCardType.htm)|
Регистрирует политику фильтрации выполнения методов расширений по любым типам
карточек. Используйте для замещения политики, назначенной посредством методов
[WhenCardTypes(IExtensionPolicyContainer,
String[])](M_Tessa_Cards_CardExtensions_WhenCardTypes_1.htm) и
[WhenCardTypes(IExtensionPolicyContainer,
Guid[])](M_Tessa_Cards_CardExtensions_WhenCardTypes.htm). Если идентификатор и
имя типа карточки неизвестны, то метод расширения не выполняется. Для того,
чтобы политика использовалась, требуется зарегистрировать политику
[CardTypeFilterPolicy](T_Tessa_Cards_Extensions_CardTypeFilterPolicy.htm).  
[WhenAnyDeleteMethod](M_Tessa_Cards_CardExtensions_WhenAnyDeleteMethod.htm)|
Регистрирует политику фильтрации выполнения методов расширений по любым
методам удаления карточки.  
[WhenAnyFileType](M_Tessa_Cards_CardExtensions_WhenAnyFileType.htm)|
Регистрирует политику фильтрации выполнения методов расширений по любым типам
файлов. Используйте для замещения политики, назначенной посредством методов
[WhenFileTypes(IExtensionPolicyContainer,
String[])](M_Tessa_Cards_CardExtensions_WhenFileTypes_1.htm) и
[WhenFileTypes(IExtensionPolicyContainer,
Guid[])](M_Tessa_Cards_CardExtensions_WhenFileTypes.htm). Если идентификатор и
имя типа файла неизвестны, то метод расширения выполняется. Для того, чтобы
политика использовалась, требуется зарегистрировать политику
[CardFileTypeFilterPolicy](T_Tessa_Cards_Extensions_CardFileTypeFilterPolicy.htm).  
[WhenAnyGetFileContentMethod](M_Tessa_Cards_CardExtensions_WhenAnyGetFileContentMethod.htm)|
Регистрирует политику фильтрации выполнения методов расширений по любым
методам загрузки контента файла.  
[WhenAnyGetFileVersionsMethod](M_Tessa_Cards_CardExtensions_WhenAnyGetFileVersionsMethod.htm)|
Регистрирует политику фильтрации выполнения методов расширений по любым
методам загрузки списка версий файла.  
[WhenAnyGetMethod](M_Tessa_Cards_CardExtensions_WhenAnyGetMethod.htm)|
Регистрирует политику фильтрации выполнения методов расширений по любым
методам загрузки карточки.  
[WhenAnyNewMethod](M_Tessa_Cards_CardExtensions_WhenAnyNewMethod.htm)|
Регистрирует политику фильтрации выполнения методов расширений по любым
методам создания карточки.  
[WhenAnyRequestType](M_Tessa_Cards_CardExtensions_WhenAnyRequestType.htm)|
Регистрирует политику фильтрации выполнения методов расширений по любым именам
универсальных запросов к сервису карточек. Используйте для замещения политики,
назначенной посредством метода [WhenRequestTypes(IExtensionPolicyContainer,
Guid[])](M_Tessa_Cards_CardExtensions_WhenRequestTypes.htm). Имя запроса
является обязательным параметром и должно быть известно. Для того, чтобы
политика использовалась, требуется зарегистрировать политику
[CardRequestFilterPolicy](T_Tessa_Cards_Extensions_CardRequestFilterPolicy.htm).  
[WhenAnyStoreMethod](M_Tessa_Cards_CardExtensions_WhenAnyStoreMethod.htm)|
Регистрирует политику фильтрации выполнения методов расширений по любым
методам сохранения карточки.  
[WhenAnyTaskType](M_Tessa_Cards_CardExtensions_WhenAnyTaskType.htm)|
Регистрирует политику фильтрации выполнения методов расширений по любым типам
заданий. Используйте для замещения политики, назначенной посредством методов
[WhenTaskTypes(IExtensionPolicyContainer,
String[])](M_Tessa_Cards_CardExtensions_WhenTaskTypes_1.htm) и
[WhenTaskTypes(IExtensionPolicyContainer,
Guid[])](M_Tessa_Cards_CardExtensions_WhenTaskTypes.htm). Если идентификатор и
имя типа задания неизвестны, то метод расширения выполняется. Для того, чтобы
политика использовалась, требуется зарегистрировать политику
[CardTaskTypeFilterPolicy](T_Tessa_Cards_Extensions_CardTaskTypeFilterPolicy.htm).  
[WhenCardDeleteFunc](M_Tessa_Cards_CardExtensions_WhenCardDeleteFunc.htm)|
Регистрирует политику фильтрации выполнения методов расширений
[ICardDeleteExtension](T_Tessa_Cards_Extensions_ICardDeleteExtension.htm) в
соответствии с функцией isAllowedFunc, которая проверяет контекст расширений.
Если зарегистрировано несколько политик, то должны выполняться все из них.  
[WhenCardGetFileContentFunc](M_Tessa_Cards_CardExtensions_WhenCardGetFileContentFunc.htm)|
Регистрирует политику фильтрации выполнения методов расширений
[ICardGetFileContentExtension](T_Tessa_Cards_Extensions_ICardGetFileContentExtension.htm)
в соответствии с функцией isAllowedFunc, которая проверяет контекст
расширений. Если зарегистрировано несколько политик, то должны выполняться все
из них.  
[WhenCardGetFileVersionsFunc](M_Tessa_Cards_CardExtensions_WhenCardGetFileVersionsFunc.htm)|
Регистрирует политику фильтрации выполнения методов расширений
[ICardGetFileVersionsExtension](T_Tessa_Cards_Extensions_ICardGetFileVersionsExtension.htm)
в соответствии с функцией isAllowedFunc, которая проверяет контекст
расширений. Если зарегистрировано несколько политик, то должны выполняться все
из них.  
[WhenCardGetFunc](M_Tessa_Cards_CardExtensions_WhenCardGetFunc.htm)|
Регистрирует политику фильтрации выполнения методов расширений
[ICardGetExtension](T_Tessa_Cards_Extensions_ICardGetExtension.htm) в
соответствии с функцией isAllowedFunc, которая проверяет контекст расширений.
Если зарегистрировано несколько политик, то должны выполняться все из них.  
[WhenCardMetadataFunc](M_Tessa_Cards_CardExtensions_WhenCardMetadataFunc.htm)|
Регистрирует политику фильтрации выполнения методов расширений
[ICardMetadataExtension](T_Tessa_Cards_Extensions_ICardMetadataExtension.htm)
в соответствии с функцией isAllowedFunc, которая проверяет контекст
расширений. Если зарегистрировано несколько политик, то должны выполняться все
из них.  
[WhenCardNewFunc](M_Tessa_Cards_CardExtensions_WhenCardNewFunc.htm)|
Регистрирует политику фильтрации выполнения методов расширений
[ICardNewExtension](T_Tessa_Cards_Extensions_ICardNewExtension.htm) в
соответствии с функцией isAllowedFunc, которая проверяет контекст расширений.
Если зарегистрировано несколько политик, то должны выполняться все из них.  
[WhenCardRepairFunc](M_Tessa_Cards_CardExtensions_WhenCardRepairFunc.htm)|
Регистрирует политику фильтрации выполнения методов расширений
[ICardRepairExtension](T_Tessa_Cards_Extensions_ICardRepairExtension.htm) в
соответствии с функцией isAllowedFunc, которая проверяет контекст расширений.
Если зарегистрировано несколько политик, то должны выполняться все из них.  
[WhenCardRequestFunc](M_Tessa_Cards_CardExtensions_WhenCardRequestFunc.htm)|
Регистрирует политику фильтрации выполнения методов расширений
[ICardRequestExtension](T_Tessa_Cards_Extensions_ICardRequestExtension.htm) в
соответствии с функцией isAllowedFunc, которая проверяет контекст расширений.
Если зарегистрировано несколько политик, то должны выполняться все из них.  
[WhenCardStoreFunc](M_Tessa_Cards_CardExtensions_WhenCardStoreFunc.htm)|
Регистрирует политику фильтрации выполнения методов расширений
[ICardStoreExtension](T_Tessa_Cards_Extensions_ICardStoreExtension.htm) в
соответствии с функцией isAllowedFunc, которая проверяет контекст расширений.
Если зарегистрировано несколько политик, то должны выполняться все из них.  
[WhenCardStoreTaskFunc](M_Tessa_Cards_CardExtensions_WhenCardStoreTaskFunc.htm)|
Регистрирует политику фильтрации выполнения методов расширений
[ICardStoreTaskExtension](T_Tessa_Cards_Extensions_ICardStoreTaskExtension.htm)
в соответствии с функцией isAllowedFunc, которая проверяет контекст
расширений. Если зарегистрировано несколько политик, то должны выполняться все
из них.  
[WhenCardTypes(IExtensionPolicyContainer,
Guid[])](M_Tessa_Cards_CardExtensions_WhenCardTypes.htm)|  Регистрирует
политику фильтрации выполнения методов расширений по идентификатору типа
карточки, который входит в заданный список идентификаторов. Если тип карточки
неизвестен, то метод расширения не выполняется. Для того, чтобы политика
использовалась, требуется зарегистрировать политику
[CardTypeFilterPolicy](T_Tessa_Cards_Extensions_CardTypeFilterPolicy.htm).  
[WhenCardTypes(IExtensionPolicyContainer,
String[])](M_Tessa_Cards_CardExtensions_WhenCardTypes_1.htm)|  Регистрирует
политику фильтрации выполнения методов расширений по имени типа карточки,
которое входит в заданный список имён. Если тип карточки неизвестен, то метод
расширения не выполняется. Для того, чтобы политика использовалась, требуется
зарегистрировать политику
[CardTypeFilterPolicy](T_Tessa_Cards_Extensions_CardTypeFilterPolicy.htm).  
[WhenFileTypes(IExtensionPolicyContainer,
Guid[])](M_Tessa_Cards_CardExtensions_WhenFileTypes.htm)|  Регистрирует
политику фильтрации выполнения методов расширений по идентификатору типа
файла, который входит в заданный список идентификаторов. Если тип файла
неизвестен, то метод расширения не выполняется. Для того, чтобы политика
использовалась, требуется зарегистрировать политику
[CardFileTypeFilterPolicy](T_Tessa_Cards_Extensions_CardFileTypeFilterPolicy.htm).  
[WhenFileTypes(IExtensionPolicyContainer,
String[])](M_Tessa_Cards_CardExtensions_WhenFileTypes_1.htm)|  Регистрирует
политику фильтрации выполнения методов расширений по имени типа файла, которое
входит в заданный список имён. Если тип файла неизвестен, то метод расширения
не выполняется. Для того, чтобы политика использовалась, требуется
зарегистрировать политику
[CardFileTypeFilterPolicy](T_Tessa_Cards_Extensions_CardFileTypeFilterPolicy.htm).  
[WhenMethod(IExtensionPolicyContainer,
CardDeleteMethod[])](M_Tessa_Cards_CardExtensions_WhenMethod.htm)|
Регистрирует политику фильтрации выполнения методов расширений по списку
допустимых методов удаления карточки.  
[WhenMethod(IExtensionPolicyContainer,
CardGetFileContentMethod[])](M_Tessa_Cards_CardExtensions_WhenMethod_1.htm)|
Регистрирует политику фильтрации выполнения методов расширений по списку
допустимых методов загрузки контента файла.  
[WhenMethod(IExtensionPolicyContainer,
CardGetFileVersionsMethod[])](M_Tessa_Cards_CardExtensions_WhenMethod_2.htm)|
Регистрирует политику фильтрации выполнения методов расширений по списку
допустимых методов загрузки списка версий файла.  
[WhenMethod(IExtensionPolicyContainer,
CardGetMethod[])](M_Tessa_Cards_CardExtensions_WhenMethod_3.htm)|
Регистрирует политику фильтрации выполнения методов расширений по списку
допустимых методов загрузки карточки.  
[WhenMethod(IExtensionPolicyContainer,
CardNewMethod[])](M_Tessa_Cards_CardExtensions_WhenMethod_4.htm)|
Регистрирует политику фильтрации выполнения методов расширений по списку
допустимых методов создания карточки.  
[WhenMethod(IExtensionPolicyContainer,
CardStoreMethod[])](M_Tessa_Cards_CardExtensions_WhenMethod_5.htm)|
Регистрирует политику фильтрации выполнения методов расширений по списку
допустимых методов сохранения карточки.  
[WhenRequestTypes](M_Tessa_Cards_CardExtensions_WhenRequestTypes.htm)|
Регистрирует политику фильтрации выполнения методов расширений по типу
универсального запроса к сервису карточек, которое входит в заданный список
типов. Тип запроса является обязательным параметром и должен быть известен.
Для того, чтобы политика использовалась, требуется зарегистрировать политику
[CardRequestFilterPolicy](T_Tessa_Cards_Extensions_CardRequestFilterPolicy.htm).  
[WhenTaskTypes(IExtensionPolicyContainer,
Guid[])](M_Tessa_Cards_CardExtensions_WhenTaskTypes.htm)|  Регистрирует
политику фильтрации выполнения методов расширений по идентификатору типа
задания, который входит в заданный список идентификаторов. Если тип задания
неизвестен, то метод расширения не выполняется. Для того, чтобы политика
использовалась, требуется зарегистрировать политику
[CardTaskTypeFilterPolicy](T_Tessa_Cards_Extensions_CardTaskTypeFilterPolicy.htm).  
[WhenTaskTypes(IExtensionPolicyContainer,
String[])](M_Tessa_Cards_CardExtensions_WhenTaskTypes_1.htm)|  Регистрирует
политику фильтрации выполнения методов расширений по имени типа задания,
которое входит в заданный список имён. Если тип задания неизвестен, то метод
расширения не выполняется. Для того, чтобы политика использовалась, требуется
зарегистрировать политику
[CardTaskTypeFilterPolicy](T_Tessa_Cards_Extensions_CardTaskTypeFilterPolicy.htm).  
[WhereInstanceType(IEnumerable<SchemeTable>,
Nullable<CardInstanceType>)](M_Tessa_Cards_CardExtensions_WhereInstanceType.htm)|
Выполняет фильтрацию таблиц по признаку их возможной принадлежности карточке
заданного типа экземпляра.  
[WhereInstanceType(IEnumerable<SchemeTable>,
CardInstanceType)](M_Tessa_Cards_CardExtensions_WhereInstanceType_1.htm)|
Выполняет фильтрацию таблиц по признаку их возможной принадлежности карточке
заданного типа экземпляра.  
[WhereSectionType(IEnumerable<SchemeTable>,
Nullable<CardSectionType>)](M_Tessa_Cards_CardExtensions_WhereSectionType.htm)|
Выполняет фильтрацию таблиц по типу секции в карточке.  
[WhereSectionType(IEnumerable<SchemeTable>,
CardSectionType)](M_Tessa_Cards_CardExtensions_WhereSectionType_1.htm)|
Выполняет фильтрацию таблиц по типу секции в карточке.  
## __См. также
#### Ссылки
[CardExtensions - ](T_Tessa_Cards_CardExtensions.htm)
[Tessa.Cards - пространство имён](N_Tessa_Cards.htm)
