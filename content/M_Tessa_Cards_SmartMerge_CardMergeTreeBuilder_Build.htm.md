# CardMergeTreeBuilder.Build - метод
##  __Definition
 **Пространство имён:** [Tessa.Cards.SmartMerge](N_Tessa_Cards_SmartMerge.htm)  
 **Сборка:** Tessa (в Tessa.dll) Версия: 3.6.0.17
C# __Копировать
     public IMergeTree<Card, CardMergeOptions> Build(
    	IMergeContext<CardMergeOptions> mergeContext,
    	IMergeMetadata metadata,
    	Card card
    )
VB __Копировать
     Public Function Build ( 
    	mergeContext As IMergeContext(Of CardMergeOptions),
    	metadata As IMergeMetadata,
    	card As Card
    ) As IMergeTree(Of Card, CardMergeOptions)
C++ __Копировать
     public:
    virtual IMergeTree<Card^, CardMergeOptions^>^ Build(
    	IMergeContext<CardMergeOptions^>^ mergeContext, 
    	IMergeMetadata^ metadata, 
    	Card^ card
    ) sealed
F# __Копировать
     abstract Build : 
            mergeContext : IMergeContext<CardMergeOptions> * 
            metadata : IMergeMetadata * 
            card : Card -> IMergeTree<Card, CardMergeOptions> 
    override Build : 
            mergeContext : IMergeContext<CardMergeOptions> * 
            metadata : IMergeMetadata * 
            card : Card -> IMergeTree<Card, CardMergeOptions> 
#### Параметры
mergeContext
[IMergeContext](T_Tessa_SmartMerge_IMergeContext_1.htm)<[CardMergeOptions](T_Tessa_Cards_SmartMerge_CardMergeOptions.htm)>
metadata [IMergeMetadata](T_Tessa_SmartMerge_IMergeMetadata.htm)
card [Card](T_Tessa_Cards_Card.htm)
#### Возвращаемое значение
[IMergeTree](T_Tessa_SmartMerge_IMergeTree_2.htm)<[Card](T_Tessa_Cards_Card.htm),
[CardMergeOptions](T_Tessa_Cards_SmartMerge_CardMergeOptions.htm)>
#### Реализации
[IMergeTreeBuilder<TMergeObject,
TMergeOptions>.Build(IMergeContext<TMergeOptions>, IMergeMetadata,
TMergeObject)](M_Tessa_SmartMerge_IMergeTreeBuilder_2_Build.htm)  
##  __См. также
#### Ссылки
[CardMergeTreeBuilder - ](T_Tessa_Cards_SmartMerge_CardMergeTreeBuilder.htm)
[Tessa.Cards.SmartMerge - пространство имён](N_Tessa_Cards_SmartMerge.htm)
