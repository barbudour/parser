# CardTypeEntryControl - свойства
##  __Свойства
[BlockSettings](P_Tessa_Cards_CardTypeControl_BlockSettings.htm)|  Настройки
блока [CardTypeBlock](T_Tessa_Cards_CardTypeBlock.htm), которые задаются для
каждого включённого в его состав объекта.  
(Унаследован от [CardTypeControl](T_Tessa_Cards_CardTypeControl.htm))  
---|---  
[Caption](P_Tessa_Cards_CardTypeContent_Caption.htm)|  Отображаемое имя
объекта.  
(Унаследован от [CardTypeContent](T_Tessa_Cards_CardTypeContent.htm))  
[ComplexColumnID](P_Tessa_Cards_CardTypeEntryControl_ComplexColumnID.htm)|
Идентификатор комплексной колонки, в которой содержится значение поля, или
null, если поле содержится в физической колонке или составлено из нескольких
физических колонок.  
[ControlSettings](P_Tessa_Cards_CardTypeControl_ControlSettings.htm)|
Настройки используемого элемента управления, тип которого задан в свойстве
[Type](P_Tessa_Cards_CardTypeControl_Type.htm).  
(Унаследован от [CardTypeControl](T_Tessa_Cards_CardTypeControl.htm))  
[DisplayFormat](P_Tessa_Cards_CardTypeEntryControl_DisplayFormat.htm)|
Формат отображаемого в текстовом виде поля.
Если задано null или пустая строка, то в текстовом виде поле будет
отображаться как значения всех колонок из списка
[PhysicalColumnIDList](P_Tessa_Cards_CardTypeEntryControl_PhysicalColumnIDList.htm),
объединённые пробелами.  
[Flags](P_Tessa_Cards_CardTypeEntryControl_Flags.htm)|  Флаги, определяющие
дополнительные атрибуты.  
[IsSealed](P_Tessa_Cards_CardSerializableObject_IsSealed.htm)| Признак того,
что объект был защищён от изменений.  
(Унаследован от
[CardSerializableObject](T_Tessa_Cards_CardSerializableObject.htm))  
[Name](P_Tessa_Cards_CardTypeControl_Name.htm)|  Имя элемента управления или
null, если имя не задано. При задании пустой строки устанавливается значение
null. Рекомендуется задавать имя, уникальное для формы.  
(Унаследован от [CardTypeControl](T_Tessa_Cards_CardTypeControl.htm))  
[Order](P_Tessa_Cards_CardTypeContent_Order.htm)|  Порядок отображения объекта
в интерфейсе карточки.  
(Унаследован от [CardTypeContent](T_Tessa_Cards_CardTypeContent.htm))  
[PhysicalColumnIDList](P_Tessa_Cards_CardTypeEntryControl_PhysicalColumnIDList.htm)|
Список идентификаторов физических колонок, которые определяют значение поля.  
[Reference](P_Tessa_Cards_CardSerializableObject_Reference.htm)|  Имя
глобального объекта, на который ссылается данный объект.  
(Унаследован от
[CardSerializableObject](T_Tessa_Cards_CardSerializableObject.htm))  
[RequiredText](P_Tessa_Cards_CardTypeEntryControl_RequiredText.htm)|
Текст, отображаемый при отсутствии значения для контрола, значение которого
должно быть обязательно задано.
Если задано null или пустая строка, то используется строка из валидатора или
строка по умолчанию.  
[SectionID](P_Tessa_Cards_CardTypeEntryControl_SectionID.htm)|  Идентификатор
секции, содержащей колонку с полем
[ComplexColumnID](P_Tessa_Cards_CardTypeEntryControl_ComplexColumnID.htm).  
[ToolTip](P_Tessa_Cards_CardTypeControl_ToolTip.htm)|  Текст всплывающей
подсказки для элемента управления или null, если имя не задано. При задании
пустой строки или строки, состоящей из пробелов, устанавливается значение
null.  
(Унаследован от [CardTypeControl](T_Tessa_Cards_CardTypeControl.htm))  
[Type](P_Tessa_Cards_CardTypeControl_Type.htm)|  Тип используемого элемента
управления.  
(Унаследован от [CardTypeControl](T_Tessa_Cards_CardTypeControl.htm))  
[XmlElementNameInternal](P_Tessa_Cards_CardTypeEntryControl_XmlElementNameInternal.htm)|
Имя XML-элемента, для которого выполняется сериализация и десериализация.  
(Переопределяет
[CardSerializableObject.XmlElementNameInternal](P_Tessa_Cards_CardSerializableObject_XmlElementNameInternal.htm))  
##  __См. также
#### Ссылки
[CardTypeEntryControl - ](T_Tessa_Cards_CardTypeEntryControl.htm)
[Tessa.Cards - пространство имён](N_Tessa_Cards.htm)
