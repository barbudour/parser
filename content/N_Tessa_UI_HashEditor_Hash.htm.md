# Tessa.UI.HashEditor.Hash - пространство имён
Элемент управления для редактирования хеш-таблиц произвольной структуры.
Объекты для отображения структуры в форме дерева и генерации по ней модели
данных.
##  __Классы
[CollectionItemNode](T_Tessa_UI_HashEditor_Hash_CollectionItemNode.htm)|  Узел
структуры хеша - элемент коллекции  
---|---  
[CollectionNode](T_Tessa_UI_HashEditor_Hash_CollectionNode.htm)|  Узел
структуры хеша - коллекция значений  
[CollectionNodeHelper](T_Tessa_UI_HashEditor_Hash_CollectionNodeHelper.htm)|
Вспомогательные методы для работы с узлами структуры хеша  
[DeleteCollectionNodeCommand](T_Tessa_UI_HashEditor_Hash_DeleteCollectionNodeCommand.htm)|  
[DeleteDictionaryKeyCommand](T_Tessa_UI_HashEditor_Hash_DeleteDictionaryKeyCommand.htm)|
Команда удаления узла структуры хеша содержащего элемент коллекции ключ-
значение  
[DictionaryItemNode](T_Tessa_UI_HashEditor_Hash_DictionaryItemNode.htm)|  Узел
структуры хеша - элемент коллекции ключ-значение  
[DictionaryNode](T_Tessa_UI_HashEditor_Hash_DictionaryNode.htm)|  Элемент
структуры хеша - коллекция ключ-значение  
[EndCollectionNode](T_Tessa_UI_HashEditor_Hash_EndCollectionNode.htm)|  Узел
окончания коллекции  
[EndDictionaryNode](T_Tessa_UI_HashEditor_Hash_EndDictionaryNode.htm)|  Узел
окончания коллекции ключ-значение  
[HashGenerationContext](T_Tessa_UI_HashEditor_Hash_HashGenerationContext.htm)|
Контекст генерации структуры хеша  
[HashNode](T_Tessa_UI_HashEditor_Hash_HashNode.htm)|  Базовый абстрактный
класс для узлов структуры хеша  
[HashRenderer](T_Tessa_UI_HashEditor_Hash_HashRenderer.htm)|  Осуществляет
преобразование структуры хеша в текстовой документ  
[HashStructureGenerator](T_Tessa_UI_HashEditor_Hash_HashStructureGenerator.htm)|
Генератор структуры хеша.  
[StartCollectionNode](T_Tessa_UI_HashEditor_Hash_StartCollectionNode.htm)|
Узел начала коллекции  
[StartDictionaryNode](T_Tessa_UI_HashEditor_Hash_StartDictionaryNode.htm)|
Узел начала коллекции ключ-значение  
[ValueNode](T_Tessa_UI_HashEditor_Hash_ValueNode.htm)|  Элемент структуры хеша
- значение элемента  
## __Интерфейсы
[ICollectionNodeDataProvider](T_Tessa_UI_HashEditor_Hash_ICollectionNodeDataProvider.htm)|
Описание интерфейса поддерживающего представление сведений о коллекции  
---|---  
[ICompositeNode<T>](T_Tessa_UI_HashEditor_Hash_ICompositeNode_1.htm)|
Описание интерфейса составного узла структуры хеша  
[IDictionaryNodeDataProvider](T_Tessa_UI_HashEditor_Hash_IDictionaryNodeDataProvider.htm)|
Описание интерфейса предоставляющего доступ к данным хранилища узла структуры
в виде коллекции ключ-значение  
[IHashGenerationContext](T_Tessa_UI_HashEditor_Hash_IHashGenerationContext.htm)|
Описание интерфейса контекста генерации структуры хеша.  
[IHashNode](T_Tessa_UI_HashEditor_Hash_IHashNode.htm)|  Описание интерфейса
узла структуры хеша  
[IHashNodeFactory](T_Tessa_UI_HashEditor_Hash_IHashNodeFactory.htm)|  Описание
интерфейса фабрики создания узлов структуры хеша  
[IHashNodeOperationVisitor](T_Tessa_UI_HashEditor_Hash_IHashNodeOperationVisitor.htm)|
Описание интерфейса операции над узлом  
[IValueOwnerHashNode](T_Tessa_UI_HashEditor_Hash_IValueOwnerHashNode.htm)|
Описание интерфейса узла структуры хеша поддерживающего хранение элемента
коллекции  
[IValueProvider](T_Tessa_UI_HashEditor_Hash_IValueProvider.htm)|  Описание
интерфейса узла, предоставляющего данные для копирования  
## __Делегаты
[HashContextMenuFactoryDelegate](T_Tessa_UI_HashEditor_Hash_HashContextMenuFactoryDelegate.htm)|
Делегат получения коллекции элементов меню для элемента структуры хеша  
---|---
