# Tessa.SmartMerge - пространство имён
## __Классы
[AsyncFuncMergeResultItem<T,
TArgs>](T_Tessa_SmartMerge_AsyncFuncMergeResultItem_2.htm)|  Представляет
объект результата слияния, который содержит в себе кастомную логику слияния  
---|---  
[MergeContext<TMergeOptions>](T_Tessa_SmartMerge_MergeContext_1.htm)|
Реализует контекст слияния.  
[MergeMetadata](T_Tessa_SmartMerge_MergeMetadata.htm)|  Содержит метаданные
для слияния  
[MergeMetadataTier](T_Tessa_SmartMerge_MergeMetadataTier.htm)|  Реализует
уровень метаданных для слияния, содержащий в себе узлы метаданных слияния  
[MergeOptions](T_Tessa_SmartMerge_MergeOptions.htm)|  Параметры слияния.  
[MergeResultBase<TMergeObject>](T_Tessa_SmartMerge_MergeResultBase_1.htm)|
Базовый класс для реализации результатов слияния  
[MergeTree<T, TMergeOptions>](T_Tessa_SmartMerge_MergeTree_2.htm)|  
[SmartMergeHelper](T_Tessa_SmartMerge_SmartMergeHelper.htm)|  
[SmartMergerBase<TMergeObject,
TMergeOptions>](T_Tessa_SmartMerge_SmartMergerBase_2.htm)|  Абстрактный
базовый класс для типичной реализации мерджера через IMergeTreeBuilder и
IMergeMetadataBuilder  
[TreeNodeBase<T>](T_Tessa_SmartMerge_TreeNodeBase_1.htm)|  
[TreeTier<T>](T_Tessa_SmartMerge_TreeTier_1.htm)|  Тир дерева для слияния.  
## __Интерфейсы
[IMergeContext<TMergeOptions>](T_Tessa_SmartMerge_IMergeContext_1.htm)|
Представляет объект контекста для логики слияния, содержащий необходимую для
этого слияния информацию  
---|---  
[IMergeMetadata](T_Tessa_SmartMerge_IMergeMetadata.htm)|  Содержит метаданные
для слияния  
[IMergeMetadataBuilder<TMergeOptions>](T_Tessa_SmartMerge_IMergeMetadataBuilder_1.htm)|
Строит метаданные для слияния  
[IMergeMetadataNode](T_Tessa_SmartMerge_IMergeMetadataNode.htm)|  Представляет
узел для метаданных слияния  
[IMergeMetadataTier](T_Tessa_SmartMerge_IMergeMetadataTier.htm)|  Представляет
уровень метаданных для слияния, содержащий в себе узлы метаданных слияния  
[IMergeOptions](T_Tessa_SmartMerge_IMergeOptions.htm)|  Представляет параметры
слияния.  
[IMergeResult<TMergeObject>](T_Tessa_SmartMerge_IMergeResult_1.htm)|
Представляет обзект содержащий в себе результаты слияния и имеет возможность
применить их к объекту с которым происходит слияние.  
[IMergeResultItem<TMergeObject>](T_Tessa_SmartMerge_IMergeResultItem_1.htm)|
Представляет результат слияния, а также логику применения этого результата к
объекту слияния  
[IMergeTree<TMergeObject,
TMergeOptions>](T_Tessa_SmartMerge_IMergeTree_2.htm)|  Представляет дерево
слияния  
[IMergeTreeBuilder<TMergeObject,
TMergeOptions>](T_Tessa_SmartMerge_IMergeTreeBuilder_2.htm)|  Строит дерево
слияния  
[ISmartMerger<TMergeObject>](T_Tessa_SmartMerge_ISmartMerger_1.htm)|
Представляет объект выполняющий слияние двух объектов одного типа.  
[ITreeNode<TMergeObject>](T_Tessa_SmartMerge_ITreeNode_1.htm)|  Представляет
узел для дерева слияния.  
[ITreeTier<TMergeObject>](T_Tessa_SmartMerge_ITreeTier_1.htm)|  Представляет
уровень в дереве слияния  
## __Перечисления
[State](T_Tessa_SmartMerge_State.htm)|  Состояния, которые может принимать
узел в дереве слияния.  
---|---
