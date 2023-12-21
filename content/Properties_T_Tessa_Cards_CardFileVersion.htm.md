# CardFileVersion - свойства
##  __Свойства
[Created](P_Tessa_Cards_CardFileVersion_Created.htm)|  Дата создания версии
(изменения файла).  
---|---  
[CreatedByID](P_Tessa_Cards_CardFileVersion_CreatedByID.htm)|  Идентификатор
пользователя, создавшего версию (изменившего файл).  
[CreatedByName](P_Tessa_Cards_CardFileVersion_CreatedByName.htm)|  Имя
пользователя, создавшего версию (изменившего файл).  
[ErrorDate](P_Tessa_Cards_CardFileVersion_ErrorDate.htm)|  Дата ошибки,
произошедшей для версии файла, или null, если ошибок не было.  
[ErrorMessage](P_Tessa_Cards_CardFileVersion_ErrorMessage.htm)|  Сообщение об
ошибке, произошедшей для версии файла, или null, если ошибок не было.  
[Hash](P_Tessa_Cards_CardFileVersion_Hash.htm)|  Хеш контента для сохранённой
версии файла или null, если версия файла новая или хеш не указан. По умолчанию
значение равно null, при этом для новых версий хеш считается не заданным.
Изменение этого значения позволяет установить другой хеш для использования в
расширениях, но не позволяет изменить хеш у версии. Для установки хеша
создаваемой версии укажите свойство [Hash](P_Tessa_Cards_CardFile_Hash.htm).  
[LinkID](P_Tessa_Cards_CardFileVersion_LinkID.htm)|  Внешний идентификатор
версии файла или null, если такой идентификатор не задан. Может использоваться
в расширениях для связи с содержимым во внешнем местоположении.  
[Name](P_Tessa_Cards_CardFileVersion_Name.htm)|  Имя версии файла.  
[Number](P_Tessa_Cards_CardFileVersion_Number.htm)|  Номер версии файла,
отсчитываемый от единицы.  
[Options](P_Tessa_Cards_CardFileVersion_Options.htm)|  Сериализованные в JSON
настройки файла. Могут быть равны null или пустой строке, если настройки не
заданы.  
[RequestInfo](P_Tessa_Cards_CardFileVersion_RequestInfo.htm)|  Дополнительная
пользовательская информация, передаваемая в запрос
[CardGetFileContentRequest](T_Tessa_Cards_CardGetFileContentRequest.htm) и в
запрос на загрузку списка подписей
[GetVersionSignatures](F_Tessa_Cards_CardRequestTypes_GetVersionSignatures.htm).  
[RowID](P_Tessa_Cards_CardFileVersion_RowID.htm)|  Идентификатор версии файла.  
[Size](P_Tessa_Cards_CardFileVersion_Size.htm)|  Размер контента в байтах для
версии файла.  
[Source](P_Tessa_Cards_CardFileVersion_Source.htm)|  Местоположение контента
версии файла.  
[State](P_Tessa_Cards_CardFileVersion_State.htm)|  Состояние версии файла.  
[Tags](P_Tessa_Cards_CardFileVersion_Tags.htm)|  Теги версии файла. Могут быть
равны null или пустой строке, если теги не заданы.  
## __См. также
#### Ссылки
[CardFileVersion - ](T_Tessa_Cards_CardFileVersion.htm)
[Tessa.Cards - пространство имён](N_Tessa_Cards.htm)
