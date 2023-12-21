# CardFile - свойства
##  __Свойства
[Card](P_Tessa_Cards_CardFile_Card.htm)|  Карточка файла.  
---|---  
[CategoryCaption](P_Tessa_Cards_CardFile_CategoryCaption.htm)|  Отображаемое
имя категории файла или null, если категория файла не указана.  
[CategoryID](P_Tessa_Cards_CardFile_CategoryID.htm)|  Идентификатор категории
файла или null, если категория файла не указана или выбранная категория не
имеет идентификатора. Значение
[CategoryCaption](P_Tessa_Cards_CardFile_CategoryCaption.htm) обязательно
должно быть указано для того, чтобы файл был включён в категорию, а значение
[CategoryID](P_Tessa_Cards_CardFile_CategoryID.htm) является опциональным для
идентификации категории.  
[Dynamic](P_Tessa_Cards_CardInfoStorageObject_Dynamic.htm)|  Объект,
осуществляющий доступ к текущему объекту через позднее связывание свойств.  
(Унаследован от
[CardInfoStorageObject](T_Tessa_Cards_CardInfoStorageObject.htm))  
[DynamicInfo](P_Tessa_Cards_CardInfoStorageObject_DynamicInfo.htm)|  Объект,
осуществляющий доступ к дополнительной пользовательской информации по текущему
объекту через позднее связывание свойств.  
(Унаследован от
[CardInfoStorageObject](T_Tessa_Cards_CardInfoStorageObject.htm))  
[ExternalSource](P_Tessa_Cards_CardFile_ExternalSource.htm)|  Внешний источник
контента для файла или null, если внешний источник отсутствует и контент для
файла загружается стандартным образом.  
[Flags](P_Tessa_Cards_CardFile_Flags.htm)|  Флаги файла.  
[Hash](P_Tessa_Cards_CardFile_Hash.htm)|  Хеш контента для последней версии
файла или null, если хеш не указан. Рекомендуется указать при создании новой
версии, чтобы в дальнейшем для этой версии был доступен хеш контента. Укажите
флаг [CalculateHash](T_Tessa_Cards_CardFileFlags.htm) в свойстве
[Flags](P_Tessa_Cards_CardFile_Flags.htm) для того, чтобы при сохранении файла
хеш-сумма была вычислена на сервере, независимо от значения в свойстве
[Hash](P_Tessa_Cards_CardFile_Hash.htm). По умолчанию значение равно null, при
этом для новых версий хеш считается не заданным.  
[Info](P_Tessa_Cards_CardInfoStorageObject_Info.htm)|  Дополнительная
пользовательская информация.  
(Унаследован от
[CardInfoStorageObject](T_Tessa_Cards_CardInfoStorageObject.htm))  
[IsVirtual](P_Tessa_Cards_CardFile_IsVirtual.htm)|  Признак того, что файл
виртуальный, такой как "Лист согласования". Некоторые расширения учитывают
этот признак, и, например, игнорируют файл при назначении разрешений в
процессе чтения карточки.  
[LastVersion](P_Tessa_Cards_CardFile_LastVersion.htm)|  Последняя версия файла
или null, если последняя версия неизвестна.  
[Name](P_Tessa_Cards_CardFile_Name.htm)|  Имя файла.  
[NewVersionTags](P_Tessa_Cards_CardFile_NewVersionTags.htm)|  Теги новой
версии файла, если такая версия будет создана в процессе сохранения. Могут
быть равны null или пустой строке, если теги не заданы, или если файл не
подготовлен для сохранения.  
[Options](P_Tessa_Cards_CardFile_Options.htm)|  Сериализованные в
типизированный JSON настройки файла. Могут быть равны null или пустой строке,
если настройки не заданы. Для установки значения рекомендуется использовать
метод [SetOptions(Dictionary<String,
Object>)](M_Tessa_Cards_CardFile_SetOptions.htm), а для получения -
[DeserializeOptions()](M_Tessa_Cards_CardFile_DeserializeOptions.htm).  
[OriginalFileID](P_Tessa_Cards_CardFile_OriginalFileID.htm)|  Идентификатор
файла, копией версии которого является текущий файл, или null, если файл
является оригиналом, а не копией.  
[OriginalVersionRowID](P_Tessa_Cards_CardFile_OriginalVersionRowID.htm)|
Идентификатор версии файла, копией которой является текущий файл, или null,
если файл является оригиналом, а не копией.  
[RequestInfo](P_Tessa_Cards_CardFile_RequestInfo.htm)|  Дополнительная
пользовательская информация, передаваемая в запросы
[CardGetFileContentRequest](T_Tessa_Cards_CardGetFileContentRequest.htm) и
[CardGetFileVersionsRequest](T_Tessa_Cards_CardGetFileVersionsRequest.htm), и
в запрос на загрузку списка подписей
[GetVersionSignatures](F_Tessa_Cards_CardRequestTypes_GetVersionSignatures.htm).  
[RowID](P_Tessa_Cards_CardFile_RowID.htm)|  Идентификатор строки с описанием
файла.  
[SectionRows](P_Tessa_Cards_CardFile_SectionRows.htm)|  Пустые строки
коллекционных и древовидных секций, доступные по имени секции. Могут
использоваться для редактирования карточки файла.  
[Size](P_Tessa_Cards_CardFile_Size.htm)|  Размер контента последней версии
файла в байтах или -1, если размер неизвестен или не был задан. В серверных
расширениях на сохранение это свойство можно использовать для определения
размера контента сохраняемых файлов.  
[State](P_Tessa_Cards_CardFile_State.htm)|  Состояние файла.  
[StoreSource](P_Tessa_Cards_CardFile_StoreSource.htm)|  Местоположение,
которое следует использовать для сохраняемого контента файла. Актуально только
для файла, для которого создаётся новая версия. По умолчанию значение равно
Database.  
[TaskID](P_Tessa_Cards_CardFile_TaskID.htm)|  Идентификатор задания, к
которому приложен файл, или null, если файл приложен к основной карточке.  
[TypeCaption](P_Tessa_Cards_CardFile_TypeCaption.htm)|  Отображаемое имя типа
файла.  
[TypeID](P_Tessa_Cards_CardFile_TypeID.htm)|  Идентификатор типа файла.  
[TypeName](P_Tessa_Cards_CardFile_TypeName.htm)|  Имя типа файла.  
[VersionNumber](P_Tessa_Cards_CardFile_VersionNumber.htm)|  Актуальная версия
файла.  
[VersionRowID](P_Tessa_Cards_CardFile_VersionRowID.htm)|  Идентификатор
актуальной версии файла.  
[Versions](P_Tessa_Cards_CardFile_Versions.htm)|  Список версий файла.
Загружается отложенно; список заполнен, если значение
[VersionsLoaded](P_Tessa_Cards_CardFile_VersionsLoaded.htm) равно true.  
[VersionsLoaded](P_Tessa_Cards_CardFile_VersionsLoaded.htm)|  Признак того,
что список версий [Versions](P_Tessa_Cards_CardFile_Versions.htm) был
загружен.  
## __См. также
#### Ссылки
[CardFile - ](T_Tessa_Cards_CardFile.htm)
[Tessa.Cards - пространство имён](N_Tessa_Cards.htm)
