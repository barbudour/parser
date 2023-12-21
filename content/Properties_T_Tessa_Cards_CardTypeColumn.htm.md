# CardTypeColumn - свойства
##  __Свойства
[AggregationFormat](P_Tessa_Cards_CardTypeColumn_AggregationFormat.htm)|
Формат агрегации дочерних строк. Если значение равно null, то строки выводятся
как есть. Если количество дочерних строк равно нулю, то результирующая строка
должна быть равна null. В противном случае соединённые сепараторами
[Separator](P_Tessa_Cards_CardTypeColumn_Separator.htm) дочерние строки
приходят в качестве параметра {0}, а количество строк - в параметре {1}. Таким
образом, например, можно поставить точку в конце списка строк, разделённые
запятыми.  
---|---  
[Alignment](P_Tessa_Cards_CardTypeColumn_Alignment.htm)|  Выравнивание
содержимого, отображаемого в колонке.  
[Caption](P_Tessa_Cards_CardTypeContent_Caption.htm)|  Отображаемое имя
объекта.  
(Унаследован от [CardTypeContent](T_Tessa_Cards_CardTypeContent.htm))  
[ComplexColumnID](P_Tessa_Cards_CardTypeColumn_ComplexColumnID.htm)|
Идентификатор комплексной колонки, в которой содержится значение поля, или
null, если поле содержится в физической колонке или составлено из нескольких
физических колонок.  
[DisplayFormat](P_Tessa_Cards_CardTypeColumn_DisplayFormat.htm)|  Формат
отображаемых в текстовом виде полей колонки. Если задано null или пустая
строка, то в текстовом виде поле будет отображаться как значение комплексной
колонки [ComplexColumnID](P_Tessa_Cards_CardTypeColumn_ComplexColumnID.htm)
или первой колонки из списка
[PhysicalColumnIDList](P_Tessa_Cards_CardTypeColumn_PhysicalColumnIDList.htm).  
[Flags](P_Tessa_Cards_CardTypeColumn_Flags.htm)|  Флаги, определяющие
дополнительные атрибуты.  
[HeaderAlignment](P_Tessa_Cards_CardTypeColumn_HeaderAlignment.htm)|
Выравнивание заголовка колонки.  
[IsSealed](P_Tessa_Cards_CardSerializableObject_IsSealed.htm)| Признак того,
что объект был защищён от изменений.  
(Унаследован от
[CardSerializableObject](T_Tessa_Cards_CardSerializableObject.htm))  
[MaxLength](P_Tessa_Cards_CardTypeColumn_MaxLength.htm)|  Максимальная
отображаемая длина колонки в ячейке таблицы. Равна null или нулю, если
ограничения отсутствуют.  
[Order](P_Tessa_Cards_CardTypeContent_Order.htm)|  Порядок отображения объекта
в интерфейсе карточки.  
(Унаследован от [CardTypeContent](T_Tessa_Cards_CardTypeContent.htm))  
[OwnedComplexColumnID](P_Tessa_Cards_CardTypeColumn_OwnedComplexColumnID.htm)|
Идентификатор комплексной колонки в дочерней секции или null, если текущий
объект не связан с дочерней секцией или связан только с её физическими
колонками.  
[OwnedOrderColumnID](P_Tessa_Cards_CardTypeColumn_OwnedOrderColumnID.htm)|
Идентификатор колонки в дочерней секции, задающей порядок отображения дочерних
строк, или null, если текущий объект не связан с дочерней секцией или дочерняя
секция не упорядочена.  
[OwnedPhysicalColumnIDList](P_Tessa_Cards_CardTypeColumn_OwnedPhysicalColumnIDList.htm)|
Список идентификаторов физических колонок, которые определяют значения полей
колонки в дочерней секции. Колонки указываются для секции
[OwnedSectionID](P_Tessa_Cards_CardTypeColumn_OwnedSectionID.htm).  
[OwnedSectionID](P_Tessa_Cards_CardTypeColumn_OwnedSectionID.htm)|
Идентификатор дочерней секции или null, если текущий объект не связан с
дочерней секцией.  
[PhysicalColumnIDList](P_Tessa_Cards_CardTypeColumn_PhysicalColumnIDList.htm)|
Список идентификаторов физических колонок, которые определяют значения полей
колонки.  
[Reference](P_Tessa_Cards_CardSerializableObject_Reference.htm)|  Имя
глобального объекта, на который ссылается данный объект.  
(Унаследован от
[CardSerializableObject](T_Tessa_Cards_CardSerializableObject.htm))  
[SelectableControlName](P_Tessa_Cards_CardTypeColumn_SelectableControlName.htm)|
Имя (алиас) контрола, который будет автоматически выбран при открытии строки
по двойному клику по ячейке в этой колонке, или null, если выделяемых
контролов нет.  
[Separator](P_Tessa_Cards_CardTypeColumn_Separator.htm)|  Разделитель между
дочерними строками.  
[ToolTipLineLength](P_Tessa_Cards_CardTypeColumn_ToolTipLineLength.htm)|
Предпочитаемая ширина всплывающей подсказки в символах. Если ширина превышает
это значение, то подсказка разбивается на несколько строк, где строки
переносятся по словам, которые разделены символами категории whitespace в
Unicode. По умолчанию значение равно
[DefaultToolTipLineLength](F_Tessa_Cards_CardTypeColumn_DefaultToolTipLineLength.htm).
Если значение равно 0, то используется
[DefaultToolTipLineLength](F_Tessa_Cards_CardTypeColumn_DefaultToolTipLineLength.htm).
Не должно быть отрицательным числом.  
[XmlElementNameInternal](P_Tessa_Cards_CardTypeColumn_XmlElementNameInternal.htm)|
Имя XML-элемента, для которого выполняется сериализация и десериализация.  
(Переопределяет
[CardSerializableObject.XmlElementNameInternal](P_Tessa_Cards_CardSerializableObject_XmlElementNameInternal.htm))  
##  __См. также
#### Ссылки
[CardTypeColumn - ](T_Tessa_Cards_CardTypeColumn.htm)
[Tessa.Cards - пространство имён](N_Tessa_Cards.htm)
